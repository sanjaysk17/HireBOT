from pydantic import BaseModel, Field
from typing import Literal, Dict

class LLMResponseModel(BaseModel):
    classification: Literal["Replied", "Unreplied", "JD Received"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    extracted_data: Dict[str, str] = {}
