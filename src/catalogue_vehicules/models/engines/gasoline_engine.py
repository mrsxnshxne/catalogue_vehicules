from catalogue_vehicules.core.interfaces.engine import Engine


class GasolineEngine(Engine):

    def __init__(self, power: int, tank_capacity: int, consumption: float):
        self.__type = "gasoline"
        self.__power = power
        self.__tank_capacity = tank_capacity
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
    def tank_capacity(self) -> int:
        return self.__tank_capacity

    @tank_capacity.setter
    def tank_capacity(self, value: int):
        self.__tank_capacity = value

    @property
    def consumption(self) -> float:
        return self.__consumption

    @consumption.setter
    def consumption(self, value: float):
        self.__consumption = value

    def get_autonomy(self) -> float:
        return self.__tank_capacity * 100 / self.__consumption