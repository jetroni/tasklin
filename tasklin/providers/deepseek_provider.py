import time
from openai import OpenAI
from ..models import AIResponse
from .base import AIProvider


class DeepSeekProvider(AIProvider):
    name = "deepseek"

    def __init__(self, api_key: str = None, model: str = None, base_url: str = None):
        super().__init__(api_key, model, base_url or "https://api.deepseek.com")

    def generate(self, prompt: str, **kwargs) -> AIResponse:
        start = time.time()
        client = OpenAI(api_key=self.api_key, base_url=self.base_url)

        resp = client.chat.completions.create(
            model=self.model or "deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )

        output = resp.choices[0].message.content.strip()
        duration = int((time.time() - start) * 1000)
        raw_data = resp.model_dump() if hasattr(resp, "model_dump") else dict(resp)
        tokens = resp.usage.total_tokens if hasattr(resp, "usage") else None

        return AIResponse(
            provider="deepseek",
            model=self.model or "deepseek-chat",
            output=output,
            raw=raw_data,
            tokens_used=tokens,
            duration_ms=duration,
        )
