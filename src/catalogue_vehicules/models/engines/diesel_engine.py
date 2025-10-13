"""
This module defines the DieselEngine class, which represents a diesel engine with specific attributes
"""

from catalogue_vehicules.core.interfaces.models.engine import Engine


class DieselEngine(Engine):
    """
    Diesel engine model
    """

    def __init__(self, power: int, tank_capacity: int, consumption: float):
        self.__type = "diesel"
        self.__power = power
        self.__tank_capacity = tank_capacity
        self.__consumption = consumption

    @property
    def type(self) -> str:
        """
        Get the type
        :return:
        """
        return self.__type

    @property
    def power(self) -> int:
        """
        Get the power of the vehicle
        :return:
        """
        return self.__power

    @power.setter
    def power(self, value: int):
        """
        Set the power of the vehicle
        :return:
        """
        self.__power = value

    @property
    def tank_capacity(self) -> int:
        """
        Get the tank capacity
        :return:
        """
        return self.__tank_capacity

    @tank_capacity.setter
    def tank_capacity(self, value: int):
        """
        Set the tank capacity
        :return:
        """
        self.__tank_capacity = value

    @property
    def consumption(self) -> float:
        """
        Get the vehicle consumption
        :return:
        """
        return self.__consumption

    @consumption.setter
    def consumption(self, value: float):
        """
        Set the vehicle consumption
        :return:
        """
        self.__consumption = value

    def get_autonomy(self) -> float:
        """
        Get the vehicle autonomy
        :return:
        """
        return self.__tank_capacity * 100 / self.__consumption
