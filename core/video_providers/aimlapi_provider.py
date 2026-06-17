import os
import time
import requests
from core.video_providers.base import BaseVideoProvider
from config import config


class AimlApiVideoProvider(BaseVideoProvider):
    """
    Video provider using AI/ML API (Wan2.1, Kling, or similar).
    Docs: https://aimlapi.com/
    """

    API_BASE = "https://api.aimlapi.com/v2"
    MODEL = "wan2.1/t2v-13B"  # Text-to-video model

    def generate_clip(self, prompt: str, duration: float, scene_number: int) -> str:
        output_path = os.path.join(config.OUTPUT_DIR, f"scene_{scene_number:02d}.mp4")
        headers = {
            "Authorization": f"Bearer {config.AIMLAPI_KEY}",
            "Content-Type": "application/json"
        }

        # Submit generation job
        resp = requests.post(
            f"{self.API_BASE}/generate/video/wan-ai/wan2.1-t2v-13b",
            headers=headers,
            json={"prompt": prompt, "duration": min(int(duration), 10)}
        )
        resp.raise_for_status()
        generation_id = resp.json()["id"]

        # Poll for completion
        video_url = self._poll(generation_id, headers)

        # Download the clip
        video_data = requests.get(video_url).content
        with open(output_path, "wb") as f:
            f.write(video_data)

        return output_path

    def _poll(self, generation_id: str, headers: dict, max_wait: int = 300) -> str:
        for _ in range(max_wait // 5):
            time.sleep(5)
            resp = requests.get(
                f"{self.API_BASE}/generate/video/wan-ai/wan2.1-t2v-13b",
                headers=headers,
                params={"generation_id": generation_id}
            )
            data = resp.json()
            status = data.get("status")
            if status == "completed":
                return data["video"]["url"]
            elif status == "failed":
                raise RuntimeError(f"Video generation failed: {data}")
        raise TimeoutError("Video generation timed out")
