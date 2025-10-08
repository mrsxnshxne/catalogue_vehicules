from catalogue_vehicules.core.interfaces.engine import Engine
from catalogue_vehicules.core.interfaces.vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self, engine: Engine, brand: str, model: str, year: int, empty_weight: int, max_weight: int, kilometers: float = 0.0):
        self.__engine = engine
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__kilometers = kilometers
        self.__empty_weight = empty_weight
        self.__max_weight = max_weight

    @property
    def engine(self) -> Engine:
        return self.__engine

    @engine.setter
    def engine(self, engine: Engine):
        self.__engine = engine

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def kilometers(self) -> float:
        return self.__kilometers

    @kilometers.setter
    def kilometers(self, kilometers: float):
        self.__kilometers = kilometers

    @property
    def empty_weight(self) -> int:
        return self.__empty_weight

    @empty_weight.setter
    def empty_weight(self, value: int):
        self.__empty_weight = value

    @property
    def max_weight(self) -> int:
        return self.__max_weight

    @max_weight.setter
    def max_weight(self, value: int):
        self.__max_weight = value