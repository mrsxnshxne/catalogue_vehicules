from abc import ABC, abstractmethod
from catalogue_vehicules.core.interfaces.engine import Engine

class Vehicle(ABC):
    @property
    @abstractmethod
    def engine(self) -> Engine:
        pass

    @engine.setter
    @abstractmethod
    def engine(self, engine: Engine):
        pass

    @property
    @abstractmethod
    def brand(self) -> str:
        pass

    @brand.setter
    @abstractmethod
    def brand(self, brand: str):
        pass

    @property
    @abstractmethod
    def model(self) -> str:
        pass

    @model.setter
    @abstractmethod
    def model(self, model: str):
        pass

    @property
    @abstractmethod
    def year(self) -> int:
        pass

    @year.setter
    @abstractmethod
    def year(self, year: int):
        pass

    @property
    @abstractmethod
    def kilometers(self) -> float:
        pass

    @kilometers.setter
    @abstractmethod
    def kilometers(self, kilometers: float):
        pass
