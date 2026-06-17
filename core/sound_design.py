import os
from pydub import AudioSegment
from core.models import VideoScript
from config import config


class SoundDesigner:
    """Mixes narration with background music and sound effects."""

    ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "audio")

    def mix(self, narration_path: str, script: VideoScript) -> str:
        """Mix narration with background music. Returns path to mixed audio."""
        output_path = os.path.join(config.OUTPUT_DIR, "mixed_audio.mp3")

        narration = AudioSegment.from_file(narration_path)
        bg_music_path = os.path.join(self.ASSETS_DIR, "background.mp3")

        if os.path.exists(bg_music_path):
            bg = AudioSegment.from_file(bg_music_path)
            bg = bg - 18  # lower background volume by 18dB
            bg = bg[:len(narration)]  # trim to narration length
            mixed = narration.overlay(bg)
        else:
            print("ℹ️  No background music found — using narration only")
            mixed = narration

        mixed.export(output_path, format="mp3")
        return output_path
