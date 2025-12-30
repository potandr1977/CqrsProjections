from dataclasses import field, dataclass
from typing import List, Callable, Dict, Any

from sqlalchemy import Boolean

from src.persons.application.saga_common.saga_step_result import SagaStepResult
from src.persons.application.saga_common.saga_step import SagaStep


@dataclass
class Saga:
    id:str
    finished:Boolean
    _steps: List[SagaStep] = field(default_factory=list)

    def add_step(
        self,
        name: str,
        action: Callable[[Dict,Dict], Any],
        compensate: Callable[[Dict,Dict], Any]
    ) -> "Saga":
        self._steps.append(SagaStep(action=action, compensate=compensate, name=name,))
        return self

    def get_next_step(self)->SagaStep:
        return next((step for step in self._steps if step.step_result is None), None)

    def get_prev_success_step(self)->SagaStep:
        return (
            next((step for step in reversed(self._steps)
                  if step.step_result is not None and step.step_result.success), None))


    async def execute_next_step(self, context: Dict | None = None, ) -> SagaStepResult | None:
        if context is None:
            context = {}

        prev_step = self.get_prev_success_step()
        prev_result = None
        if prev_step is not None:
            prev_result = prev_step.step_result.result

        cur_step = self.get_next_step()
        if cur_step is None:
            return None
        try:
            cur_step._context = context
            action_result =  await cur_step.action(context, prev_result)
            cur_step.step_result = SagaStepResult(
                success=True,
                result=action_result,
            )

            return cur_step.step_result
        except Exception as e:
            print(f"⛔ Error in step: {cur_step.name}: {e}")
            # откатываем в обратном порядке
            cur_step.step_result = SagaStepResult(
                success=False,
                result=context,
                error_step=cur_step.name,
                error=e,
            )

            cur_step.compensate(context,prev_result)

            return cur_step.step_result

