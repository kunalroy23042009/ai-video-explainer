from pydantic import BaseModel
from typing import List, Optional


class Scene(BaseModel):
    """A single scene in the explainer video."""
    scene_number: int
    title: str
    narration: str
    visual_prompt: str  # Prompt sent to video generation API
    duration_seconds: float = 5.0


class VideoScript(BaseModel):
    """Full script for an explainer video."""
    topic: str
    title: str
    scenes: List[Scene]
    total_duration: float = 0.0

    def model_post_init(self, __context):
        self.total_duration = sum(s.duration_seconds for s in self.scenes)
