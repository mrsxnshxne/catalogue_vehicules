"""
Service for managing electric engines.
"""

from catalogue_vehicules.core.interfaces.services.engine_service import EngineService
from catalogue_vehicules.models.engines.electric_engine import ElectricEngine


class ElectricEngineService(EngineService):
    """
    Service class for managing
    """

    def __init__(self):
        """
        Initialize the CarService with an empty data store and last index set to 0.

        Returns:
            None
        """
        self.__last_index: int = 0
        self.__data: dict[int, ElectricEngine] = {}

    def get(self) -> list[ElectricEngine]:
        """
        Get all engines in the catalogue.

        Returns:
            list[Engine]: List of all engines.

        Example:
            service = ElectricEngineService()
            cars = service.get()
        """
        values = []
        for _, value in self.__data.items():
            values.append(value)
        return values

    def find(self, engine_id: int) -> ElectricEngine:
        """
        Find an electric engine by its ID.

        Args:
            engine_id (int): ID of the electric engine to find.

        Returns:
            ElectricEngine: The electric engine with the given ID.

        Example:
            service = CarService()
            car = service.find(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Electric engine not found")
        return self.__data[engine_id]

    def create(self, data: dict) -> bool:
        """
        Create a new electric engine and add it to the catalogue.

        Args:
            data (dict): Data for the new electric engine.

        Returns:
            bool: True if the electric engine was created successfully.

        Example:
            service = ElectricEngineService()
            data = {
                "engine_power_electric": 150,
                "engine_battery_capacity": 75,
                "engine_battery_consumption": 15,
            }
        """
        engine = ElectricEngine(
            power=data["engine_power_electric"],
            battery_capacity=data["engine_battery_capacity"],
            consumption=data["engine_battery_consumption"],
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = engine
        self.__last_index = last_index

        return True

    def delete(self, engine_id: int):
        """
        Delete an electric engine by its ID.

        Args:
            engine_id (int): ID of the electric engine to delete.

        Returns:
            None

        Example:
            service = ElectricEngineService()
            service.delete(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Electric engine not found")
        del self.__data[engine_id]
