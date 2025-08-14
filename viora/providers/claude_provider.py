import time
from anthropic import Anthropic
from ..models import AIResponse
from .base import AIProvider


class ClaudeProvider(AIProvider):
    name = "claude"

    def generate(self, prompt: str, **kwargs) -> AIResponse:
        start = time.time()
        client = Anthropic(api_key=self.api_key, base_url=self.base_url)

        max_tokens = kwargs.get('max_tokens', 1024)
        temperature = kwargs.get('temperature', None)
        system = kwargs.get('system', None)

        request_params = {
            "model": self.model or "claude-3-5-sonnet-20241022",
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}]
        }

        if temperature is not None:
            request_params["temperature"] = temperature
        if system:
            request_params["system"] = system

        resp = client.messages.create(**request_params)

        output = resp.content[0].text.strip() if resp.content else ""
        duration = int((time.time() - start) * 1000)
        raw_data = resp.model_dump() if hasattr(resp, "model_dump") else dict(resp)

        tokens = None
        if hasattr(resp, "usage"):
            tokens = resp.usage.input_tokens + resp.usage.output_tokens

        return AIResponse(
            provider="claude",
            model=self.model or "claude-3-5-sonnet-20241022",
            output=output,
            raw=raw_data,
            tokens_used=tokens,
            duration_ms=duration
        )