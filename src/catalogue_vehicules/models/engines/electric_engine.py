"""
Electric engine model
"""

from catalogue_vehicules.core.interfaces.models.engine import Engine


class ElectricEngine(Engine):

    def __init__(self, power: int, battery_capacity: int, consumption: float):
        self.__type = "electric"
        self.__power = power
        self.__battery_capacity = battery_capacity
        self.__consumption = consumption

    @property
    def type(self) -> str:
        return self.__type

    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, value: int):
        self.__power = value

    @property
    def battery_capacity(self) -> int:
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value: int):
        self.__battery_capacity = value

    @property
    def consumption(self) -> float:
        return self.__consumption

    @consumption.setter
    def consumption(self, value: float):
        self.__consumption = value

    def get_autonomy(self) -> float:
        return self.__battery_capacity * 100 / self.__consumption
