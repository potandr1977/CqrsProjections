from abc import abstractmethod, ABC


class ICartService(ABC):
    @abstractmethod
    def get_rep_name(self):
        pass