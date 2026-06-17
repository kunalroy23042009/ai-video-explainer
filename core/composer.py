import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from core.models import VideoScript
from core.video_providers import get_provider
from config import config


class VideoComposer:
    """Assembles scene videos + audio into a final MP4."""

    def compose(self, script: VideoScript, audio_path: str, output_path: str) -> str:
        provider = get_provider(config.VIDEO_PROVIDER)
        scene_clips = []

        for scene in script.scenes:
            clip_path = provider.generate_clip(
                prompt=scene.visual_prompt,
                duration=scene.duration_seconds,
                scene_number=scene.scene_number
            )
            scene_clips.append(VideoFileClip(clip_path))

        final_video = concatenate_videoclips(scene_clips)
        audio = AudioFileClip(audio_path)

        # Trim audio/video to same length
        min_dur = min(final_video.duration, audio.duration)
        final_video = final_video.subclip(0, min_dur)
        audio = audio.subclip(0, min_dur)

        final_video = final_video.set_audio(audio)
        final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

        return output_path
