"""
This module defines the HybridEngine class, which represents a hybrid engine
"""

from catalogue_vehicules.core.interfaces.models.engine import Engine


class HybridEngine(Engine):
    """
    Hybrid engine class
    """

    def __init__(
        self,
        power_gasoline: int,
        power_electric: int,
        tank_capacity: int,
        battery_capacity: int,
        tank_consumption: float,
        battery_consumption: float,
    ):
        self.__type = "hybrid"
        self.__power = round((power_gasoline + power_electric) * 0.7, 0)
        self.__power_gasoline = power_gasoline
        self.__power_electric = power_electric
        self.__tank_capacity = tank_capacity
        self.__battery_capacity = battery_capacity
        self.__tank_consumption = tank_consumption
        self.__battery_consumption = battery_consumption

    @property
    def type(self) -> str:
        """
        Get the type of the engine
        :return:
        """
        return self.__type

    @property
    def power(self) -> float:
        """
        Get the power of the engine
        :return:
        """
        return self.__power

    @property
    def power_gasoline(self) -> int:
        """
        Get the power of the gasoline engine
        :return:
        """
        return self.__power_gasoline

    @power_gasoline.setter
    def power_gasoline(self, value: int):
        """
        Set the power of the gasoline engine
        :param value:
        :return:
        """
        self.__power_gasoline = value
        self.__power = round((self.__power_gasoline + self.__power_electric) * 0.7, 0)

    @property
    def power_electric(self) -> int:
        """
        Get the power of the electric engine
        :return:
        """
        return self.__power_electric

    @power_electric.setter
    def power_electric(self, value: int):
        """
        Set the power of the electric engine
        :param value:
        :return:
        """
        self.__power_electric = value
        self.__power = round((self.__power_gasoline + self.__power_electric) * 0.7, 0)

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
        :param value:
        :return:
        """
        self.__tank_capacity = value

    @property
    def battery_capacity(self) -> int:
        """
        Get the battery capacity
        :return:
        """
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value: int):
        """
        Set the battery capacity
        :param value:
        :return:
        """
        self.__battery_capacity = value

    @property
    def tank_consumption(self) -> float:
        """
        Get the tank consumption
        :return:
        """
        return self.__tank_consumption

    @tank_consumption.setter
    def tank_consumption(self, value: float):
        """
        Set the tank consumption
        :param value:
        :return:
        """
        self.__tank_consumption = value

    @property
    def battery_consumption(self) -> float:
        """
        Get the battery consumption
        :return:
        """
        return self.__battery_consumption

    @battery_consumption.setter
    def battery_consumption(self, value: float):
        """
        Set the battery consumption
        :param value:
        :return:
        """
        self.__battery_consumption = value

    def get_autonomy(self) -> float:
        """
        Get the vehicle autonomy
        :return:
        """
        return (
            self.__tank_capacity * 100 / self.__tank_consumption
            + self.__battery_capacity * 100 / self.__battery_consumption
        )
