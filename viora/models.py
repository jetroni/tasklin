from pydantic import BaseModel
from typing import Any, Dict, Optional


class AIResponse(BaseModel):
    provider: str
    model: str
    output: str
    raw: Dict[str, Any]
    tokens_used: Optional[int] = None
    duration_ms: Optional[int] = None
