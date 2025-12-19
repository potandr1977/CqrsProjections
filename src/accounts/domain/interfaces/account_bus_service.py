from abc import abstractmethod, ABC

from src.accounts.domain.models.account import Account
from src.events import AccountCreated


class IAccountBusService(ABC):
    @abstractmethod
    async def public_account_created(self, account_created: AccountCreated)->Account:...
