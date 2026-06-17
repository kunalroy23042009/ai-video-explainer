from core.video_providers.base import BaseVideoProvider
from core.video_providers.stub_provider import StubVideoProvider
from core.video_providers.aimlapi_provider import AimlApiVideoProvider


def get_provider(name: str) -> BaseVideoProvider:
    """Factory — returns the right provider by name."""
    providers = {
        "stub": StubVideoProvider,
        "aimlapi": AimlApiVideoProvider,
    }
    cls = providers.get(name)
    if not cls:
        raise ValueError(f"Unknown video provider: {name}. Choose from: {list(providers.keys())}")
    return cls()
