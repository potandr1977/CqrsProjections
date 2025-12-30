from dataclasses import dataclass

from src.persons.application.create_person_saga.CreateAccountHandler import create_account, compensate_create_account
from src.persons.application.create_person_saga.CreatePaymentHandler import create_payment, compensate_create_payment
from src.persons.application.create_person_saga.CreatePersonHandler import create_person, compensate_create_person
from src.persons.application.saga_common.saga import Saga

@dataclass
class CreatePersonSaga(Saga):
    def __init__(self, id:str, finished:bool = False):
        super().__init__(id=id,finished=finished)
        self.add_step(
            action = create_person,
            compensate = compensate_create_person,
            name="Create Person"
        )

        self.add_step(
            action=create_account,
            compensate=compensate_create_account,
            name="Create Account"
        )

        # self.add_step(
        #     action=lambda ctx, prev_result: create_person(ctx,prev_result),
        #     compensate=lambda ctx, prev_result: create_person(ctx,prev_result),
        #     name="Create Account"
        # )
        #
        # self.add_step(
        #     action=lambda ctx, prev_result: create_person(ctx,prev_result),
        #     compensate=lambda ctx, prev_result: create_person(ctx,prev_result),
        #     name="Create Payment"
        # )



