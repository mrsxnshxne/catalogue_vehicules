from abc import ABC, abstractmethod

class Engine(ABC):
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
    def get_autonomy(self) -> float:
        pass
