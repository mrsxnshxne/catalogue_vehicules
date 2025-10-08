from abc import ABC, abstractmethod

class Engine(ABC):

    def __init__(self, type: str, power: int):
        self._type = type
        self._power = power

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def power(self) -> int:
        pass

    @power.setter
    @abstractmethod
    def power(self, power: int):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass
