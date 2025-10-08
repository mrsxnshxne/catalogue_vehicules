from catalogue_vehicules.core.interfaces.engine import Engine
from catalogue_vehicules.core.interfaces.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, engine: Engine, brand: str, model: str, year: int, trunk_volume: int, category: str, kilometers: float = 0.0):
        self.__engine = engine
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__kilometers = kilometers
        self.__trunk_volume = trunk_volume
        self.__category = category

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
    def storage(self) -> int:
        return self.__trunk_volume

    @storage.setter
    def storage(self, trunk_volume: int):
        self.__trunk_volume = trunk_volume

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category