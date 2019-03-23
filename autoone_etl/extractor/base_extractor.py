from abc import abstractmethod, ABC


class BaseExtractor(ABC):
    def __init__(self) -> None:
        super().__init__()

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def close(self):
        pass