from dataclasses import dataclass
from typing import Any


@dataclass
class SagaStepResult:
    result:Any
    success: bool
    error_step: str | None = None
    error: Exception | None = None