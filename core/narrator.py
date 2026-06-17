import subprocess
import os
import tempfile
from core.models import VideoScript
from config import config


class Narrator:
    """Converts script narration to audio using Piper TTS."""

    def synthesize(self, script: VideoScript) -> str:
        """Synthesize full narration and return path to WAV file."""
        full_narration = " ".join(scene.narration for scene in script.scenes)
        output_path = os.path.join(config.OUTPUT_DIR, "narration.wav")

        try:
            result = subprocess.run(
                ["piper", "--model", config.PIPER_VOICE, "--output_file", output_path],
                input=full_narration.encode(),
                capture_output=True,
                timeout=60
            )
            if result.returncode != 0:
                raise RuntimeError(f"Piper TTS failed: {result.stderr.decode()}")
        except FileNotFoundError:
            print("⚠️  Piper not found — generating silent placeholder audio")
            self._generate_silent(output_path, len(script.scenes) * 5)

        return output_path

    def _generate_silent(self, path: str, duration: int):
        """Generate a silent WAV as fallback."""
        from pydub import AudioSegment
        silent = AudioSegment.silent(duration=duration * 1000)
        silent.export(path, format="wav")
