"""
Hinglish Text Processing Utilities
Handles mixed Hindi-English text processing for TTS optimization
"""

import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import unicodedata

@dataclass
class HinglishSegment:
    """Represents a segment of Hinglish text with language annotation"""
    text: str
    language: str  # 'hi', 'en', or 'mixed'
    is_technical: bool = False
    pronunciation_hint: Optional[str] = None

class HinglishProcessor:
    """Processes Hinglish text for optimal TTS rendering"""
    
    def __init__(self):
        # Common English technical terms used in Indian education
        self.technical_terms = {
            # Physics terms
            'force', 'mass', 'acceleration', 'velocity', 'momentum', 'energy', 
            'kinetic', 'potential', 'electromagnetic', 'frequency', 'amplitude',
            'wavelength', 'newton', 'joule', 'watt', 'volt', 'ampere', 'ohm',
            'gravity', 'friction', 'pressure', 'temperature', 'thermodynamics',
            
            # Chemistry terms  
            'atom', 'molecule', 'electron', 'proton', 'neutron', 'orbital',
            'covalent', 'ionic', 'hydrogen', 'oxygen', 'carbon', 'nitrogen',
            'periodic', 'element', 'compound', 'reaction', 'catalyst', 'ph',
            'acid', 'base', 'oxidation', 'reduction', 'molar', 'molarity',
            
            # Biology terms
            'cell', 'nucleus', 'cytoplasm', 'membrane', 'mitochondria', 'dna',
            'rna', 'protein', 'enzyme', 'chromosome', 'gene', 'photosynthesis',
            'respiration', 'metabolism', 'homeostasis', 'evolution', 'ecosystem',
            'biodiversity', 'species', 'population', 'community',
            
            # Math terms
            'equation', 'formula', 'variable', 'constant', 'coefficient',
            'derivative', 'integral', 'matrix', 'vector', 'scalar', 'sine',
            'cosine', 'tangent', 'logarithm', 'exponential', 'polynomial'
        }
        
        # Hindi-English word mappings for common educational terms
        self.hindi_mappings = {
            'देखिए': 'dekhiye',
            'समझिए': 'samjhiye', 
            'यहाँ': 'yahan',
            'वहाँ': 'vahan',
            'कैसे': 'kaise',
            'क्यों': 'kyon',
            'क्या': 'kya',
            'जब': 'jab',
            'तब': 'tab',
            'अगर': 'agar',
            'तो': 'to',
            'और': 'aur',
            'या': 'ya',
            'लेकिन': 'lekin',
            'इसलिए': 'isliye',
            'क्योंकि': 'kyonki'
        }
        
        # Pronunciation adjustments for technical terms in Hindi context
        self.pronunciation_adjustments = {
            'acceleration': 'एक्सेलेरेशन',
            'electromagnetic': 'इलेक्ट्रोमैग्नेटिक', 
            'photosynthesis': 'फोटोसिंथेसिस',
            'thermodynamics': 'थर्मोडायनामिक्स',
            'chromosome': 'क्रोमोसोम',
            'mitochondria': 'माइटोकॉन्ड्रिया'
        }
    
    def detect_language_segments(self, text: str) -> List[HinglishSegment]:
        """Detect and segment text by language (Hindi/English/Mixed)"""
        segments = []
        
        # Split by sentences first
        sentences = re.split(r'[।.!?]+', text)
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            # Analyze character composition
            hindi_chars = len(re.findall(r'[\u0900-\u097F]', sentence))
            english_chars = len(re.findall(r'[a-zA-Z]', sentence))
            total_chars = hindi_chars + english_chars
            
            if total_chars == 0:
                continue
            
            hindi_ratio = hindi_chars / total_chars
            
            # Classify segment
            if hindi_ratio > 0.7:
                language = 'hi'
            elif hindi_ratio < 0.3:
                language = 'en'
            else:
                language = 'mixed'
            
            # Check for technical terms
            words = sentence.lower().split()
            has_technical = any(word.strip('.,!?()[]') in self.technical_terms for word in words)
            
            segments.append(HinglishSegment(
                text=sentence,
                language=language,
                is_technical=has_technical
            ))
        
        return segments
    
    def romanize_hindi(self, text: str) -> str:
        """Convert Hindi Devanagari text to romanized form for TTS"""
        # Simple mapping - in production, use a proper transliteration library
        romanized = text
        
        for hindi, roman in self.hindi_mappings.items():
            romanized = romanized.replace(hindi, roman)
        
        return romanized
    
    def enhance_technical_pronunciation(self, text: str) -> str:
        """Enhance pronunciation of technical terms in Hindi context"""
        enhanced = text
        
        for term, pronunciation in self.pronunciation_adjustments.items():
            # Replace technical terms with pronunciation hints
            pattern = r'\b' + re.escape(term) + r'\b'
            enhanced = re.sub(pattern, f"{term} ({pronunciation})", enhanced, flags=re.IGNORECASE)
        
        return enhanced
    
    def process_for_tts(self, text: str, service: str = 'xtts') -> str:
        """Process Hinglish text for optimal TTS rendering"""
        
        # Normalize Unicode characters
        text = unicodedata.normalize('NFKC', text)
        
        # Clean up text
        text = self._clean_text(text)
        
        # Detect segments
        segments = self.detect_language_segments(text)
        
        processed_segments = []
        
        for segment in segments:
            processed_text = segment.text
            
            if service == 'gtts':
                # For gTTS, romanize Hindi text
                if segment.language in ['hi', 'mixed']:
                    processed_text = self.romanize_hindi(processed_text)
            
            elif service == 'xtts':
                # For XTTS, enhance technical term pronunciation
                if segment.is_technical:
                    processed_text = self.enhance_technical_pronunciation(processed_text)
            
            # Add pronunciation pauses for better flow
            processed_text = self._add_natural_pauses(processed_text)
            
            processed_segments.append(processed_text)
        
        return ' '.join(processed_segments)
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Fix punctuation spacing
        text = re.sub(r'\s*([।.!?,:;])\s*', r'\1 ', text)
        
        # Remove special characters that might confuse TTS
        text = re.sub(r'[^\u0900-\u097F\w\s।.!?,:;()\-\'\"]+', '', text)
        
        return text.strip()
    
    def _add_natural_pauses(self, text: str) -> str:
        """Add natural pauses for better speech flow"""
        # Add slight pause after conjunctions
        conjunctions = ['और', 'aur', 'लेकिन', 'lekin', 'तो', 'to', 'इसलिए', 'isliye']
        for conj in conjunctions:
            text = re.sub(f'\\b{conj}\\b', f'{conj},', text)
        
        # Add pause before technical explanations
        text = re.sub(r'(\w+)\s+(means|matlab|yaani)', r'\1, \2', text)
        
        return text
    
    def create_ssml(self, text: str, voice_config: Dict) -> str:
        """Create SSML markup for enhanced TTS control"""
        
        # Process text first
        processed_text = self.process_for_tts(text, 'xtts')
        
        # Build SSML
        ssml = f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="hi">'
        
        # Add voice characteristics
        if 'speaking_rate' in voice_config:
            rate = voice_config['speaking_rate']
            ssml += f'<prosody rate="{rate:.2f}">'
        
        # Add emphasis to technical terms
        segments = self.detect_language_segments(processed_text)
        
        for segment in segments:
            if segment.is_technical:
                ssml += f'<emphasis level="moderate">{segment.text}</emphasis> '
            else:
                ssml += f'{segment.text} '
        
        # Close prosody tags
        if 'speaking_rate' in voice_config:
            ssml += '</prosody>'
        
        ssml += '</speak>'
        
        return ssml
    
    def validate_hinglish_text(self, text: str) -> Tuple[bool, List[str]]:
        """Validate Hinglish text and return issues"""
        issues = []
        
        # Check for empty text
        if not text.strip():
            issues.append("Text is empty")
            return False, issues
        
        # Check for excessive English in Hindi-focused content
        segments = self.detect_language_segments(text)
        english_segments = [s for s in segments if s.language == 'en']
        
        if len(english_segments) > len(segments) * 0.7:
            issues.append("Text appears to be mostly English - consider adding more Hindi")
        
        # Check for missing technical term context
        technical_segments = [s for s in segments if s.is_technical]
        for segment in technical_segments:
            words = segment.text.lower().split()
            technical_words = [w for w in words if w.strip('.,!?()[]') in self.technical_terms]
            
            if len(technical_words) > 3:
                issues.append(f"Segment has many technical terms - consider simplifying: {segment.text[:50]}...")
        
        # Check for proper sentence structure
        if not re.search(r'[।.!?]$', text.strip()):
            issues.append("Text should end with proper punctuation")
        
        return len(issues) == 0, issues

# Global processor instance
hinglish_processor = HinglishProcessor()
