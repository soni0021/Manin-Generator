"""
TTS Configuration for Hinglish Educational Content
Supports multiple TTS services with fallback mechanisms
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional
from enum import Enum
import os

class TTSQuality(Enum):
    """TTS Quality levels"""
    FAST = "fast"      # gTTS for quick prototyping
    HIGH = "high"      # XTTS v2 for production
    PREMIUM = "premium" # ElevenLabs for premium content

class SubjectVoice(Enum):
    """Subject-specific voice personas"""
    PHYSICS = "physics"
    CHEMISTRY = "chemistry"
    BIOLOGY = "biology"
    GENERAL = "general"

@dataclass
class XTTSConfig:
    """Configuration for Coqui XTTS v2"""
    model_name: str = "tts_models/multilingual/multi-dataset/xtts_v2"
    language: str = "hi"
    speaker_wav: Optional[str] = None
    temperature: float = 0.75
    length_penalty: float = 1.0
    repetition_penalty: float = 5.0
    top_k: int = 50
    top_p: float = 0.85
    speed: float = 1.0
    enable_text_splitting: bool = True
    
    # Hindi fine-tuned model settings
    use_finetuned_model: bool = True
    finetuned_model_path: str = "Abhinay45/XTTS-Hindi-finetuned"
    
@dataclass
class GTTSConfig:
    """Configuration for Google TTS"""
    lang: str = "hi"
    slow: bool = False
    domain: str = "com"
    
@dataclass
class ElevenLabsConfig:
    """Configuration for ElevenLabs TTS"""
    api_key: Optional[str] = None
    voice_id: str = "pNInz6obpgDQGcFmaJgB"  # Adam voice
    model_id: str = "eleven_multilingual_v2"
    stability: float = 0.5
    similarity_boost: float = 0.75
    style: float = 0.0
    use_speaker_boost: bool = True

class TTSServiceConfig:
    """Main TTS Service Configuration"""
    
    def __init__(self):
        self.default_quality = TTSQuality.HIGH
        self.cache_dir = "/Users/manishsoni/Manin Animations/assets/audio_cache"
        self.reference_voices_dir = "/Users/manishsoni/Manin Animations/assets/reference_voices"
        
        # Service configurations
        self.xtts_config = XTTSConfig()
        self.gtts_config = GTTSConfig()
        self.elevenlabs_config = ElevenLabsConfig()
        
        # Voice profiles for different subjects
        self.voice_profiles = self._setup_voice_profiles()
        
        # Ensure cache directory exists
        os.makedirs(self.cache_dir, exist_ok=True)
        os.makedirs(self.reference_voices_dir, exist_ok=True)
    
    def _setup_voice_profiles(self) -> Dict[SubjectVoice, Dict[str, Any]]:
        """Setup voice profiles for different subjects"""
        return {
            SubjectVoice.PHYSICS: {
                "speaker_wav": f"{self.reference_voices_dir}/physics_teacher.wav",
                "temperature": 0.7,
                "speed": 0.95,
                "style_description": "Clear, authoritative physics teacher"
            },
            SubjectVoice.CHEMISTRY: {
                "speaker_wav": f"{self.reference_voices_dir}/chemistry_teacher.wav", 
                "temperature": 0.75,
                "speed": 1.0,
                "style_description": "Enthusiastic chemistry professor"
            },
            SubjectVoice.BIOLOGY: {
                "speaker_wav": f"{self.reference_voices_dir}/biology_teacher.wav",
                "temperature": 0.8,
                "speed": 1.05,
                "style_description": "Warm, nurturing biology teacher"
            },
            SubjectVoice.GENERAL: {
                "speaker_wav": f"{self.reference_voices_dir}/general_teacher.wav",
                "temperature": 0.75,
                "speed": 1.0,
                "style_description": "Friendly general educator"
            }
        }
    
    def get_service_config(self, quality: TTSQuality, subject: SubjectVoice) -> Dict[str, Any]:
        """Get configuration for specific TTS service and subject"""
        base_config = {}
        
        if quality == TTSQuality.HIGH:
            base_config = {
                "service": "xtts",
                **self.xtts_config.__dict__,
                **self.voice_profiles[subject]
            }
        elif quality == TTSQuality.FAST:
            base_config = {
                "service": "gtts",
                **self.gtts_config.__dict__
            }
        elif quality == TTSQuality.PREMIUM:
            base_config = {
                "service": "elevenlabs",
                **self.elevenlabs_config.__dict__
            }
            
        return base_config

# Global configuration instance
tts_config = TTSServiceConfig()
