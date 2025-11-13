"""
Service for managing diesel engines.
"""

from catalogue_vehicules.core.interfaces.services.engine_service import EngineService
from catalogue_vehicules.models.engines.diesel_engine import DieselEngine


class DieselEngineService(EngineService):
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
        self.__data: dict[int, DieselEngine] = {}

    def get(self) -> list[DieselEngine]:
        """
        Get all engines in the catalogue.

        Returns:
            list[Engine]: List of all engines.

        Example:
            service = DieselEngineService()
            cars = service.get()
        """
        values = []
        for _, value in self.__data.items():
            values.append(value)
        return values

    def find(self, engine_id: int) -> DieselEngine:
        """
        Find a diesel engine by its ID.

        Args:
            engine_id (int): ID of the diesel engine to find.

        Returns:
            DieselEngine: The diesel engine with the given ID.

        Example:
            service = CarService()
            car = service.find(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Diesel engine not found")
        return self.__data[engine_id]

    def create(self, data: dict) -> bool:
        """
        Create a new diesel engine and add it to the catalogue.

        Args:
            data (dict): Data for the new diesel engine.

        Returns:
            bool: True if the diesel engine was created successfully.

        Example:
            service = DieselEngineService()
            data = {
                "engine_power_diesel": 150,
                "engine_battery_capacity": 75,
                "engine_battery_consumption": 15,
            }
        """
        engine = DieselEngine(
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
        Delete a diesel engine by its ID.

        Args:
            engine_id (int): ID of the diesel engine to delete.

        Returns:
            None

        Example:
            service = DieselEngineService()
            service.delete(1)
        """
        if engine_id not in self.__data:
            raise ValueError("Diesel engine not found")
        del self.__data[engine_id]
