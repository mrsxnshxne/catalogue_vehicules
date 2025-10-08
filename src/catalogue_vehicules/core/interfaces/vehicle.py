from abc import ABC, abstractmethod

from catalogue_vehicules.core.interfaces.engine import Engine


class Vehicle(ABC):

    def __init__(self, engine: Engine, brand: str, model: str, year: int):
        self.engine = engine
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def drive(self):
        pass