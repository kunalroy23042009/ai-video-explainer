from core.script_writer import ScriptWriter
from core.narrator import Narrator
from core.sound_design import SoundDesigner
from core.composer import VideoComposer
from core.models import VideoScript
from config import config


class VideoPipeline:
    """Orchestrates the full prompt → video pipeline."""

    def __init__(self):
        self.script_writer = ScriptWriter()
        self.narrator = Narrator()
        self.sound_designer = SoundDesigner()
        self.composer = VideoComposer()

    def run(self, prompt: str, output_path: str) -> str:
        print("📝 Step 1/4: Writing script...")
        script: VideoScript = self.script_writer.generate(prompt)

        print("🎙️  Step 2/4: Generating narration...")
        audio_path = self.narrator.synthesize(script)

        print("🎵 Step 3/4: Adding sound design...")
        mixed_audio = self.sound_designer.mix(audio_path, script)

        print("🎞️  Step 4/4: Composing video...")
        video_path = self.composer.compose(script, mixed_audio, output_path)

        return video_path
