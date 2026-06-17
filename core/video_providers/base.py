from abc import ABC, abstractmethod


class BaseVideoProvider(ABC):
    """Abstract base class for video generation providers."""

    @abstractmethod
    def generate_clip(self, prompt: str, duration: float, scene_number: int) -> str:
        """
        Generate a video clip for a scene.

        Args:
            prompt: Visual description of the scene
            duration: Clip duration in seconds
            scene_number: Scene index (for naming output files)

        Returns:
            Path to the generated video clip (MP4)
        """
        ...
