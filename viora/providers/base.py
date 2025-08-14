from abc import ABC, abstractmethod
import asyncio

from ..models import AIResponse


class AIProvider(ABC):
    name: str

    def __init__(self, api_key: str = None, model: str = None, base_url: str = None):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> AIResponse:
        """Synchronous generate method."""
        raise NotImplementedError

    async def agenerate(self, prompt: str, **kwargs) -> AIResponse:
        """Async generate method (default wraps sync)."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.generate, prompt, **kwargs)
