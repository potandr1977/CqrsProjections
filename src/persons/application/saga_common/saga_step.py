from dataclasses import dataclass
from typing import Callable, Dict, Any, Coroutine, Awaitable

from src.persons.application.saga_common.saga_step_result import SagaStepResult


@dataclass
class SagaStep:
    name: str
    action: Callable[[Dict, Any], Awaitable[Any]]
    compensate: Callable[[Dict, Any], Awaitable[Any]]
    step_result: SagaStepResult = None
    _context: Dict = None