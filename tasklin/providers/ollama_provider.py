import httpx
import time
from ..models import AIResponse
from .base import AIProvider


class OllamaProvider(AIProvider):
    name = "ollama"

    def __init__(self, api_key: str = None, model: str = None, base_url: str = "http://localhost:11434"):
        super().__init__(api_key, model, base_url)
        self.base_url = base_url.rstrip("/")

    def generate(self, prompt: str, **kwargs) -> AIResponse:
        start = time.time()
        model_name = self.model or "llama3.2"

        resp = httpx.post(
            f"{self.base_url}/api/generate",
            json={"model": model_name, "prompt": prompt, "stream": False}
        )
        data = resp.json()
        output = data.get("response", "").strip()
        duration = int((time.time() - start) * 1000)

        return AIResponse(
            provider="ollama",
            model=model_name,
            output=output,
            raw=data,
            duration_ms=duration
        )
