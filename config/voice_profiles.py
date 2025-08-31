"""
Voice Profile Management for Subject-Specific Educational Content
Handles voice cloning, reference audio management, and subject-specific TTS settings
"""

from typing import Dict, List, Optional, Tuple
import os
import json
from pathlib import Path
from .tts_config import SubjectVoice, TTSQuality

class VoiceProfileManager:
    """Manages voice profiles for different educational subjects"""
    
    def __init__(self, reference_voices_dir: str = "/Users/manishsoni/Manin Animations/assets/reference_voices"):
        self.reference_voices_dir = Path(reference_voices_dir)
        self.reference_voices_dir.mkdir(parents=True, exist_ok=True)
        
        # Voice profile metadata
        self.profile_metadata_file = self.reference_voices_dir / "profiles.json"
        self.profiles = self._load_profiles()
    
    def _load_profiles(self) -> Dict[str, Dict]:
        """Load voice profile metadata from JSON file"""
        if self.profile_metadata_file.exists():
            with open(self.profile_metadata_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Create default profiles
            default_profiles = self._create_default_profiles()
            self._save_profiles(default_profiles)
            return default_profiles
    
    def _save_profiles(self, profiles: Dict[str, Dict]) -> None:
        """Save voice profile metadata to JSON file"""
        with open(self.profile_metadata_file, 'w', encoding='utf-8') as f:
            json.dump(profiles, f, indent=2, ensure_ascii=False)
    
    def _create_default_profiles(self) -> Dict[str, Dict]:
        """Create default voice profiles for each subject"""
        return {
            "physics": {
                "name": "Dr. Physics",
                "description": "Clear, authoritative physics teacher with slight Indian accent",
                "language": "hi",
                "gender": "male",
                "age_range": "35-45",
                "accent": "Indian English + Hindi",
                "speaking_rate": 0.95,
                "pitch_range": "medium",
                "energy_level": "moderate",
                "pronunciation_style": "precise",
                "reference_audio": "physics_teacher.wav",
                "sample_text": "Dekho, yeh Newton ka second law hai. Force equals mass times acceleration.",
                "technical_terms_handling": "english_pronunciation_in_hindi_flow"
            },
            "chemistry": {
                "name": "Prof. Chemistry",
                "description": "Enthusiastic chemistry professor with expressive delivery",
                "language": "hi", 
                "gender": "female",
                "age_range": "30-40",
                "accent": "Indian English + Hindi",
                "speaking_rate": 1.0,
                "pitch_range": "medium-high",
                "energy_level": "high",
                "pronunciation_style": "expressive",
                "reference_audio": "chemistry_teacher.wav",
                "sample_text": "Yeh water molecule hai. Oxygen aur hydrogen atoms covalent bond se jude hain.",
                "technical_terms_handling": "clear_english_with_hindi_explanation"
            },
            "biology": {
                "name": "Dr. Bio",
                "description": "Warm, nurturing biology teacher with patient delivery",
                "language": "hi",
                "gender": "female", 
                "age_range": "28-38",
                "accent": "Indian English + Hindi",
                "speaking_rate": 1.05,
                "pitch_range": "medium",
                "energy_level": "gentle",
                "pronunciation_style": "nurturing",
                "reference_audio": "biology_teacher.wav",
                "sample_text": "Cell membrane dekhte hain. Yeh phospholipid bilayer structure hai.",
                "technical_terms_handling": "simplified_english_with_hindi_context"
            },
            "general": {
                "name": "Teacher",
                "description": "Friendly general educator for multi-subject content",
                "language": "hi",
                "gender": "neutral",
                "age_range": "25-45", 
                "accent": "Indian English + Hindi",
                "speaking_rate": 1.0,
                "pitch_range": "medium",
                "energy_level": "moderate",
                "pronunciation_style": "friendly",
                "reference_audio": "general_teacher.wav",
                "sample_text": "Aaj hum sikhenge interesting concepts ke baare mein.",
                "technical_terms_handling": "balanced_english_hindi_mix"
            }
        }
    
    def get_profile(self, subject: SubjectVoice) -> Dict:
        """Get voice profile for a specific subject"""
        subject_key = subject.value
        return self.profiles.get(subject_key, self.profiles["general"])
    
    def update_profile(self, subject: SubjectVoice, updates: Dict) -> None:
        """Update voice profile for a subject"""
        subject_key = subject.value
        if subject_key in self.profiles:
            self.profiles[subject_key].update(updates)
            self._save_profiles(self.profiles)
    
    def get_reference_audio_path(self, subject: SubjectVoice) -> Optional[str]:
        """Get path to reference audio file for voice cloning"""
        profile = self.get_profile(subject)
        audio_file = self.reference_voices_dir / profile["reference_audio"]
        
        if audio_file.exists():
            return str(audio_file)
        else:
            # Return None if reference audio doesn't exist
            # System will use default voice
            return None
    
    def create_reference_audio_placeholder(self, subject: SubjectVoice) -> str:
        """Create placeholder reference audio file with instructions"""
        profile = self.get_profile(subject)
        audio_file = self.reference_voices_dir / profile["reference_audio"]
        instructions_file = audio_file.with_suffix('.txt')
        
        instructions = f"""
Reference Audio Instructions for {profile['name']} ({subject.value.title()})

To create a high-quality voice clone for {subject.value} content:

1. AUDIO REQUIREMENTS:
   - Duration: 10-30 seconds
   - Format: WAV, 22050 Hz, mono
   - Quality: Clear, no background noise
   - Content: Read the sample text below naturally

2. SAMPLE TEXT TO RECORD:
   "{profile['sample_text']}"

3. VOICE CHARACTERISTICS:
   - Gender: {profile['gender']}
   - Age: {profile['age_range']} years
   - Accent: {profile['accent']}
   - Style: {profile['pronunciation_style']}
   - Energy: {profile['energy_level']}

4. RECORDING TIPS:
   - Speak naturally in Hinglish (mix of Hindi and English)
   - Pronounce technical terms clearly
   - Maintain consistent pace and tone
   - Record in a quiet environment

5. FILE PLACEMENT:
   Save the recorded audio as: {audio_file}

Once you place the audio file, the system will automatically use it for voice cloning.
"""
        
        with open(instructions_file, 'w', encoding='utf-8') as f:
            f.write(instructions)
        
        return str(instructions_file)
    
    def validate_reference_audio(self, subject: SubjectVoice) -> Tuple[bool, str]:
        """Validate reference audio file for a subject"""
        audio_path = self.get_reference_audio_path(subject)
        
        if not audio_path:
            instructions_file = self.create_reference_audio_placeholder(subject)
            return False, f"Reference audio not found. Instructions created: {instructions_file}"
        
        # Basic file validation
        audio_file = Path(audio_path)
        if not audio_file.exists():
            return False, f"Audio file does not exist: {audio_path}"
        
        if audio_file.stat().st_size < 1000:  # Less than 1KB
            return False, f"Audio file too small (likely empty): {audio_path}"
        
        return True, f"Reference audio validated: {audio_path}"
    
    def list_available_profiles(self) -> List[Dict]:
        """List all available voice profiles with their status"""
        profile_list = []
        
        for subject in SubjectVoice:
            profile = self.get_profile(subject)
            is_valid, status = self.validate_reference_audio(subject)
            
            profile_list.append({
                "subject": subject.value,
                "name": profile["name"],
                "description": profile["description"],
                "has_reference_audio": is_valid,
                "status": status,
                "config": profile
            })
        
        return profile_list

# Global voice profile manager instance
voice_manager = VoiceProfileManager()
