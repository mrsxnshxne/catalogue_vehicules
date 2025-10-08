from abc import ABC, abstractmethod
from catalogue_vehicules.core.interfaces.engine import Engine

class Vehicle(ABC):

    def __init__(self, engine: Engine, brand: str, model: str, year: int, kilometers: int = 0):
        self._engine = engine
        self._brand = brand
        self._model = model
        self._year = year
        self._kilometers = kilometers

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
    def kilometers(self) -> int:
        pass

    @kilometers.setter
    @abstractmethod
    def kilometers(self, kilometers: int):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def park(self):
        pass
