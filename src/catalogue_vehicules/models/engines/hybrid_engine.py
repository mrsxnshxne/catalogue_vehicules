from catalogue_vehicules.core.interfaces.engine import Engine


class HybridEngine(Engine):

    def __init__(self, power_gasoline: int, power_electric: int, tank_capacity: int, battery_capacity: int, tank_consumption: float, battery_consumption: float):
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
        return super().type

    @property
    def power(self) -> int:
        return super().power

    @property
    def power_gasoline(self) -> int:
        return self.__power_gasoline

    @power_gasoline.setter
    def power_gasoline(self, value: int):
        self.__power_gasoline = value
        self.__power = round((self.__power_gasoline + self.__power_electric) * 0.7, 0)

    @property
    def power_electric(self) -> int:
        return self.__power_electric

    @power_electric.setter
    def power_electric(self, value: int):
        self.__power_electric = value
        self.__power = round((self.__power_gasoline + self.__power_electric) * 0.7, 0)

    @property
    def tank_capacity(self) -> int:
        return self.__tank_capacity

    @tank_capacity.setter
    def tank_capacity(self, value: int):
        self.__tank_capacity = value

    @property
    def battery_capacity(self) -> int:
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value: int):
        self.__battery_capacity = value

    @property
    def tank_consumption(self) -> float:
        return self.__tank_consumption

    @tank_consumption.setter
    def tank_consumption(self, value: float):
        self.__tank_consumption = value

    @property
    def battery_consumption(self) -> float:
        return self.__battery_consumption

    @battery_consumption.setter
    def battery_consumption(self, value: float):
        self.__battery_consumption = value

    def get_autonomy(self) -> float:
        return self.__tank_capacity * 100 / self.__tank_consumption + self.__battery_capacity * 100 / self.__battery_consumption