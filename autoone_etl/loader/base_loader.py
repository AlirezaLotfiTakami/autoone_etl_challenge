from abc import abstractmethod, ABC


class BaseLoader(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def load_next(self, data):
        pass

    @abstractmethod
    def get_results(self):
        pass

    @abstractmethod
    def close(self):
        pass
