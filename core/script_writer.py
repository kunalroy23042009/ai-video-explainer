import json
from openai import OpenAI
from core.models import VideoScript, Scene
from config import config


SYSTEM_PROMPT = """You are an expert educational content writer.
Given a topic or question, create a short animated explainer script for students.
Return a JSON object with this structure:
{
  "title": "...",
  "scenes": [
    {
      "scene_number": 1,
      "title": "...",
      "narration": "...",
      "visual_prompt": "cartoon illustration of ...",
      "duration_seconds": 5
    }
  ]
}
Keep it to 4-6 scenes. Make narration simple, engaging, and age-appropriate."""


class ScriptWriter:
    def __init__(self):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)

    def generate(self, prompt: str) -> VideoScript:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Create an explainer video script about: {prompt}"}
            ],
            response_format={"type": "json_object"}
        )
        data = json.loads(response.choices[0].message.content)
        scenes = [Scene(scene_number=i+1, **s) for i, s in enumerate(data["scenes"])]
        return VideoScript(topic=prompt, title=data["title"], scenes=scenes)
