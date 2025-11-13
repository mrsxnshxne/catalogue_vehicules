"""
Service for managing gasoline engines.
"""

from catalogue_vehicules.core.interfaces.services.engine_service import EngineService
from catalogue_vehicules.models.engines.gasoline_engine import GasolineEngine


class GasolineEngineService(EngineService):
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
        self.__data: dict[int, GasolineEngine] = {}

    def get(self) -> list[GasolineEngine]:
        """
        Get all engines in the catalogue.

        Returns:
            list[Engine]: List of all engines.

        Example:
            service = GasolineEngineService()
            cars = service.get()
        """
        values = []
        for _, value in self.__data.items():
            values.append(value)
        return values

    def find(self, engine_id: int) -> GasolineEngine:
        """
        Find a gasoline engine by its ID.

        Args:
            engine_id (int): ID of the gasoline engine to find.

        Returns:
            GasolineEngine: The gasoline engine with the given ID.

        Example:
            service = CarService()
            car = service.find(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Gasoline engine not found")
        return self.__data[engine_id]

    def create(self, data: dict) -> bool:
        """
        Create a new gasoline engine and add it to the catalogue.

        Args:
            data (dict): Data for the new gasoline engine.

        Returns:
            bool: True if the gasoline engine was created successfully.

        Example:
            service = GasolineEngineService()
            data = {
                "engine_power_gasoline": 150,
                "engine_battery_capacity": 75,
                "engine_battery_consumption": 15,
            }
        """
        engine = GasolineEngine(
            power=data["engine_power_gasoline"],
            tank_capacity=data["engine_tank_capacity"],
            consumption=data["engine_tank_consumption"],
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = engine
        self.__last_index = last_index

        return True

    def delete(self, engine_id: int):
        """
        Delete a gasoline engine by its ID.

        Args:
            engine_id (int): ID of the gasoline engine to delete.

        Returns:
            None

        Example:
            service = GasolineEngineService()
            service.delete(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Gasoline engine not found")
        del self.__data[engine_id]
