from dataclasses import dataclass
from typing import Callable, Dict, Any

from src.persons.application.saga_common.saga_step_result import SagaStepResult


@dataclass
class SagaStep:
    name: str
    context: Dict
    action: Callable[[Dict, Dict], Any]
    compensate: Callable[[Dict, Dict], Any]
    step_result: SagaStepResult = None