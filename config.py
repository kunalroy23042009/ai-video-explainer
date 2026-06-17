import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AIMLAPI_KEY: str = os.getenv("AIMLAPI_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    VIDEO_PROVIDER: str = os.getenv("VIDEO_PROVIDER", "stub")
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "./output")
    PIPER_VOICE: str = os.getenv("PIPER_VOICE", "en_US-lessac-medium")

config = Config()
