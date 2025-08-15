import time
from openai import OpenAI
from ..models import AIResponse
from .base import AIProvider


class OpenAIProvider(AIProvider):
    name = "openai"

    def generate(self, prompt: str, **kwargs) -> AIResponse:
        start = time.time()
        client = OpenAI(api_key=self.api_key)
        resp = client.chat.completions.create(
            model=self.model or "gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        output = resp.choices[0].message.content.strip()
        duration = int((time.time() - start) * 1000)
        raw_data = resp.model_dump() if hasattr(resp, "model_dump") else dict(resp)
        tokens = resp.usage.total_tokens if hasattr(resp, "usage") else None

        return AIResponse(
            provider="openai",
            model=self.model or "gpt-4o-mini",
            output=output,
            raw=raw_data,
            tokens_used=tokens,
            duration_ms=duration,
        )
