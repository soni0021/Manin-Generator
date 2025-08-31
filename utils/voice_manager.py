"""
Multi-TTS Service Manager for Hinglish Educational Content
Handles XTTS v2, gTTS, and ElevenLabs with intelligent fallback
"""

import os
import hashlib
import logging
from typing import Optional, Dict, Any, Union, List
from pathlib import Path
import tempfile
from abc import ABC, abstractmethod

# Import TTS services
try:
    import TTS
    from TTS.api import TTS as CoquiTTS
    XTTS_AVAILABLE = True
except ImportError:
    XTTS_AVAILABLE = False
    logging.warning("Coqui TTS not available. Install with: pip install TTS")

try:
    import gtts
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    logging.warning("gTTS not available. Install with: pip install gtts")

try:
    import elevenlabs
    from elevenlabs import generate, save
    ELEVENLABS_AVAILABLE = True
except ImportError:
    ELEVENLABS_AVAILABLE = False
    logging.warning("ElevenLabs not available. Install with: pip install elevenlabs")

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config.tts_config import TTSQuality, SubjectVoice, tts_config
from config.voice_profiles import voice_manager
from utils.hinglish_processor import hinglish_processor

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TTSServiceBase(ABC):
    """Abstract base class for TTS services"""
    
    @abstractmethod
    def synthesize(self, text: str, output_path: str, **kwargs) -> bool:
        """Synthesize speech and save to file"""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if service is available"""
        pass

class XTTSService(TTSServiceBase):
    """Coqui XTTS v2 service with Hindi fine-tuning support"""
    
    def __init__(self):
        self.model = None
        self.model_loaded = False
        
    def _load_model(self, config: Dict[str, Any]) -> bool:
        """Load XTTS model with configuration"""
        if not XTTS_AVAILABLE:
            return False
            
        try:
            if config.get('use_finetuned_model', True):
                # Try to load fine-tuned Hindi model
                model_path = config.get('finetuned_model_path', 'Abhinay45/XTTS-Hindi-finetuned')
                logger.info(f"Loading fine-tuned XTTS model: {model_path}")
                self.model = CoquiTTS(model_path)
            else:
                # Load default multilingual model
                model_name = config.get('model_name', 'tts_models/multilingual/multi-dataset/xtts_v2')
                logger.info(f"Loading default XTTS model: {model_name}")
                self.model = CoquiTTS(model_name)
                
            self.model_loaded = True
            return True
            
        except Exception as e:
            logger.error(f"Failed to load XTTS model: {e}")
            self.model_loaded = False
            return False
    
    def synthesize(self, text: str, output_path: str, **kwargs) -> bool:
        """Synthesize speech using XTTS"""
        if not self.is_available():
            return False
            
        config = kwargs.get('config', {})
        
        # Load model if not already loaded
        if not self.model_loaded:
            if not self._load_model(config):
                return False
        
        try:
            # Get speaker reference audio
            speaker_wav = config.get('speaker_wav')
            if speaker_wav and not os.path.exists(speaker_wav):
                logger.warning(f"Speaker reference audio not found: {speaker_wav}")
                speaker_wav = None
            
            # Synthesize speech
            if speaker_wav:
                # Voice cloning mode
                self.model.tts_to_file(
                    text=text,
                    file_path=output_path,
                    speaker_wav=speaker_wav,
                    language=config.get('language', 'hi'),
                    split_sentences=config.get('enable_text_splitting', True)
                )
            else:
                # Default voice mode
                self.model.tts_to_file(
                    text=text,
                    file_path=output_path,
                    language=config.get('language', 'hi'),
                    split_sentences=config.get('enable_text_splitting', True)
                )
            
            return os.path.exists(output_path)
            
        except Exception as e:
            logger.error(f"XTTS synthesis failed: {e}")
            return False
    
    def is_available(self) -> bool:
        """Check if XTTS is available"""
        return XTTS_AVAILABLE

class GTTSService(TTSServiceBase):
    """Google Text-to-Speech service"""
    
    def synthesize(self, text: str, output_path: str, **kwargs) -> bool:
        """Synthesize speech using gTTS"""
        if not self.is_available():
            return False
            
        config = kwargs.get('config', {})
        
        try:
            # Process text for gTTS
            processed_text = hinglish_processor.process_for_tts(text, 'gtts')
            
            # Create gTTS object
            tts = gTTS(
                text=processed_text,
                lang=config.get('lang', 'hi'),
                slow=config.get('slow', False),
                domain=config.get('domain', 'com')
            )
            
            # Save audio
            tts.save(output_path)
            return os.path.exists(output_path)
            
        except Exception as e:
            logger.error(f"gTTS synthesis failed: {e}")
            return False
    
    def is_available(self) -> bool:
        """Check if gTTS is available"""
        return GTTS_AVAILABLE

class ElevenLabsService(TTSServiceBase):
    """ElevenLabs TTS service"""
    
    def synthesize(self, text: str, output_path: str, **kwargs) -> bool:
        """Synthesize speech using ElevenLabs"""
        if not self.is_available():
            return False
            
        config = kwargs.get('config', {})
        api_key = config.get('api_key') or os.getenv('ELEVENLABS_API_KEY')
        
        if not api_key:
            logger.error("ElevenLabs API key not provided")
            return False
        
        try:
            # Set API key
            elevenlabs.set_api_key(api_key)
            
            # Generate audio
            audio = generate(
                text=text,
                voice=config.get('voice_id', 'pNInz6obpgDQGcFmaJgB'),
                model=config.get('model_id', 'eleven_multilingual_v2')
            )
            
            # Save audio
            save(audio, output_path)
            return os.path.exists(output_path)
            
        except Exception as e:
            logger.error(f"ElevenLabs synthesis failed: {e}")
            return False
    
    def is_available(self) -> bool:
        """Check if ElevenLabs is available"""
        return ELEVENLABS_AVAILABLE and (
            os.getenv('ELEVENLABS_API_KEY') is not None
        )

class HinglishTTSManager:
    """Main TTS manager with intelligent service selection and fallback"""
    
    def __init__(self):
        self.services = {
            'xtts': XTTSService(),
            'gtts': GTTSService(), 
            'elevenlabs': ElevenLabsService()
        }
        
        self.cache_dir = Path(tts_config.cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Service priority order for fallback
        self.service_priority = ['xtts', 'elevenlabs', 'gtts']
    
    def _generate_cache_key(self, text: str, quality: TTSQuality, subject: SubjectVoice) -> str:
        """Generate cache key for audio file"""
        content = f"{text}_{quality.value}_{subject.value}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def _get_cached_audio(self, cache_key: str) -> Optional[str]:
        """Get cached audio file if exists"""
        cache_file = self.cache_dir / f"{cache_key}.wav"
        if cache_file.exists():
            return str(cache_file)
        return None
    
    def _save_to_cache(self, cache_key: str, audio_path: str) -> None:
        """Save audio to cache"""
        cache_file = self.cache_dir / f"{cache_key}.wav"
        
        # Copy audio file to cache
        import shutil
        try:
            shutil.copy2(audio_path, cache_file)
        except Exception as e:
            logger.warning(f"Failed to cache audio: {e}")
    
    def _get_service_for_quality(self, quality: TTSQuality) -> str:
        """Get preferred service for quality level"""
        service_map = {
            TTSQuality.FAST: 'gtts',
            TTSQuality.HIGH: 'xtts', 
            TTSQuality.PREMIUM: 'elevenlabs'
        }
        return service_map.get(quality, 'gtts')
    
    def _get_available_services(self) -> List[str]:
        """Get list of available TTS services"""
        return [name for name, service in self.services.items() if service.is_available()]
    
    def synthesize_speech(
        self, 
        text: str, 
        output_path: str,
        quality: TTSQuality = TTSQuality.HIGH,
        subject: SubjectVoice = SubjectVoice.GENERAL,
        use_cache: bool = True
    ) -> bool:
        """
        Synthesize speech with intelligent service selection and fallback
        
        Args:
            text: Text to synthesize
            output_path: Output audio file path
            quality: TTS quality level
            subject: Subject area for voice selection
            use_cache: Whether to use audio caching
            
        Returns:
            bool: Success status
        """
        
        # Validate and process text
        is_valid, issues = hinglish_processor.validate_hinglish_text(text)
        if not is_valid:
            logger.warning(f"Text validation issues: {issues}")
        
        # Process text for TTS
        processed_text = hinglish_processor.process_for_tts(text)
        
        # Check cache first
        if use_cache:
            cache_key = self._generate_cache_key(processed_text, quality, subject)
            cached_audio = self._get_cached_audio(cache_key)
            if cached_audio:
                logger.info(f"Using cached audio: {cache_key}")
                import shutil
                shutil.copy2(cached_audio, output_path)
                return True
        
        # Get service configuration
        service_config = tts_config.get_service_config(quality, subject)
        preferred_service = self._get_service_for_quality(quality)
        
        # Try preferred service first, then fallback
        available_services = self._get_available_services()
        
        if not available_services:
            logger.error("No TTS services available")
            return False
        
        # Order services by preference
        services_to_try = []
        if preferred_service in available_services:
            services_to_try.append(preferred_service)
        
        # Add remaining services as fallback
        for service in self.service_priority:
            if service in available_services and service != preferred_service:
                services_to_try.append(service)
        
        # Try each service
        for service_name in services_to_try:
            logger.info(f"Attempting synthesis with {service_name}")
            
            service = self.services[service_name]
            
            # Create temporary file for synthesis
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
                temp_path = temp_file.name
            
            try:
                success = service.synthesize(
                    processed_text, 
                    temp_path,
                    config=service_config
                )
                
                if success and os.path.exists(temp_path):
                    # Move to final output path
                    import shutil
                    shutil.move(temp_path, output_path)
                    
                    # Cache the result
                    if use_cache:
                        self._save_to_cache(cache_key, output_path)
                    
                    logger.info(f"Successfully synthesized with {service_name}")
                    return True
                    
            except Exception as e:
                logger.error(f"Service {service_name} failed: {e}")
                
            finally:
                # Clean up temp file
                if os.path.exists(temp_path):
                    os.unlink(temp_path)
        
        logger.error("All TTS services failed")
        return False
    
    def get_service_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all TTS services"""
        status = {}
        
        for name, service in self.services.items():
            is_available = service.is_available()
            
            service_info = {
                'available': is_available,
                'name': name.upper(),
            }
            
            if name == 'xtts':
                service_info['features'] = ['voice_cloning', 'multilingual', 'high_quality']
                service_info['requirements'] = 'pip install TTS'
                
            elif name == 'gtts':
                service_info['features'] = ['fast', 'simple', 'reliable']
                service_info['requirements'] = 'pip install gtts'
                
            elif name == 'elevenlabs':
                service_info['features'] = ['premium_quality', 'voice_cloning', 'api_key_required']
                service_info['requirements'] = 'pip install elevenlabs + API key'
                service_info['api_key_set'] = bool(os.getenv('ELEVENLABS_API_KEY'))
            
            status[name] = service_info
        
        return status
    
    def clear_cache(self) -> int:
        """Clear audio cache and return number of files removed"""
        cache_files = list(self.cache_dir.glob('*.wav'))
        
        for cache_file in cache_files:
            try:
                cache_file.unlink()
            except Exception as e:
                logger.warning(f"Failed to delete cache file {cache_file}: {e}")
        
        return len(cache_files)

# Global TTS manager instance
tts_manager = HinglishTTSManager()
