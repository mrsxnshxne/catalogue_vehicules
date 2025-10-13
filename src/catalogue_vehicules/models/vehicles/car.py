from catalogue_vehicules.core.interfaces.models.engine import Engine
from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, engine: Engine, brand: str, model: str, year: int, kilometers: float, trunk: int):
        self.__engine = engine
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__kilometers = kilometers
        self.__trunk = trunk

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
    def trunk(self) -> int:
        return self.__trunk

    @trunk.setter
    def trunk(self, trunk: int):
        self.__trunk = trunk

    def __str__(self) -> str:
        return f"Car(brand={self.__brand}, model={self.__model}, year={self.__year}, kilometers={self.__kilometers}, trunk={self.__trunk}, engine={self.__engine})"