from src.persons.application.create_person_saga.CreateAccount import create_account, compensate_create_account
from src.persons.application.create_person_saga.CreatePayment import create_payment, compensate_create_payment
from src.persons.application.create_person_saga.CreatePerson import create_person, compensate_create_person
from src.persons.application.saga_common.saga import Saga


class CreatePersonSaga(Saga):
    def __init__(self):
        (
            self.add_step(
                action= lambda ctx: create_person(ctx),
                compensate= lambda ctx: compensate_create_person(ctx),
                name="Create Person"
            ).
            add_step(
                action=lambda ctx: create_account(ctx),
                compensate=lambda ctx: compensate_create_account(ctx),
                name="Create Account"
            ).
            add_step(
                action=lambda ctx: create_payment(ctx),
                compensate=lambda ctx: compensate_create_payment(ctx),
                name="Create Account"
            )
        )


