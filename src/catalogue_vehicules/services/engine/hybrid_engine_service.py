"""
Service for managing hybrid engines.
"""

from catalogue_vehicules.core.interfaces.services.engine_service import EngineService
from catalogue_vehicules.models.engines.hybrid_engine import HybridEngine


class HybridEngineService(EngineService):
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
        self.__data: dict[int, HybridEngine] = {}

    def get(self) -> list[HybridEngine]:
        """
        Get all engines in the catalogue.

        Returns:
            list[Engine]: List of all engines.

        Example:
            service = HybridEngineService()
            cars = service.get()
        """
        values = []
        for _, value in self.__data.items():
            values.append(value)
        return values

    def find(self, engine_id: int) -> HybridEngine:
        """
        Find a hybrid engine by its ID.

        Args:
            engine_id (int): ID of the hybrid engine to find.

        Returns:
            HybridEngine: The hybrid engine with the given ID.

        Example:
            service = CarService()
            car = service.find(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Hybrid engine not found")
        return self.__data[engine_id]

    def create(self, data: dict) -> bool:
        """
        Create a new hybrid engine and add it to the catalogue.

        Args:
            data (dict): Data for the new hybrid engine.

        Returns:
            bool: True if the hybrid engine was created successfully.

        Example:
            service = HybridEngineService()
            data = {
                "engine_power_hybrid": 150,
                "engine_battery_capacity": 75,
                "engine_battery_consumption": 15,
            }
        """
        engine = HybridEngine(
            power_gasoline=data["engine_power_gasoline"],
            power_electric=data["engine_power_electric"],
            battery_capacity=data["engine_battery_capacity"],
            tank_capacity=data["engine_tank_capacity"],
            battery_consumption=data["engine_battery_consumption"],
            tank_consumption=data["engine_tank_consumption"],
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = engine
        self.__last_index = last_index

        return True

    def delete(self, engine_id: int):
        """
        Delete a hybrid engine by its ID.

        Args:
            engine_id (int): ID of the hybrid engine to delete.

        Returns:
            None

        Example:
            service = HybridEngineService()
            service.delete(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Hybrid engine not found")
        del self.__data[engine_id]
