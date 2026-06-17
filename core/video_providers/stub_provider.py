import os
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
from core.video_providers.base import BaseVideoProvider
from config import config


class StubVideoProvider(BaseVideoProvider):
    """
    Stub provider for local testing — generates a colored placeholder clip
    with the scene prompt as text overlay. No API calls needed.
    """

    COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD"]

    def generate_clip(self, prompt: str, duration: float, scene_number: int) -> str:
        output_path = os.path.join(config.OUTPUT_DIR, f"scene_{scene_number:02d}.mp4")
        color = self.COLORS[(scene_number - 1) % len(self.COLORS)]

        bg = ColorClip(size=(1280, 720), color=self._hex_to_rgb(color), duration=duration)

        txt = TextClip(
            f"Scene {scene_number}\n{prompt[:80]}",
            fontsize=32, color="white", font="DejaVu-Sans",
            size=(1100, None), method="caption"
        ).set_position("center").set_duration(duration)

        clip = CompositeVideoClip([bg, txt])
        clip.write_videofile(output_path, fps=24, codec="libx264", logger=None)
        return output_path

    @staticmethod
    def _hex_to_rgb(hex_color: str):
        h = hex_color.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
