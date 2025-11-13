"""
Service for managing trucks in the vehicle catalogue.
"""

from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle
from catalogue_vehicules.core.interfaces.services.vehicule_service import VehicleService
from catalogue_vehicules.models.vehicles.truck import Truck
from catalogue_vehicules.utils.utils import create_engine_helper
from catalogue_vehicules.utils.validators.truck_validator import validate_truck_data


class TruckService(VehicleService):
    """
    Service class for managing trucks in the vehicle catalogue.
    """

    def __init__(self):
        """
        Initialize the TruckService with an empty data store and last index set to 0.

        Returns:
            None
        """
        self.__last_index: int = 0
        self.__data: dict[int, Truck] = {}

    def get(self,  engine: str | None = None) -> list[Vehicle]:
        """
        Get all trucks in the catalogue.

        Returns:
            list[Vehicle]: List of all trucks.

        Example:
            service = TruckService()
            trucks = service.get()
        """
        values = []
        for _, value in self.__data.items():
            if engine is None or value.engine.type == engine:
                values.append(value)
        return values

    def find(self, vehicle_id: int) -> Vehicle:
        """
        Find a truck by its ID.

        Args:
            vehicle_id (int): ID of the truck to find.

        Returns:
            Vehicle: The truck with the given ID.

        Example:
            service = TruckService()
            truck = service.find(1)
        """
        if vehicle_id not in self.__data:
            raise ValueError("Truck not found")
        return self.__data[vehicle_id]

    @validate_truck_data
    def create(self, data: dict) -> bool:
        """
        Create a new truck and add it to the catalogue.

        Args:
            data (dict): Data for the new truck.

        Returns:
            bool: True if the truck was created successfully.

        Example:
            service = TruckService()
            data = {
                "brand": "Volvo",
                "model": "FH16",
                "year": 2021,
                "kilometers": 120000,
                "max_weight": 40000,
                "engine_type": "diesel",
                "engine_power": 520,
                "engine_capacity": 13000,
                "engine_consumption": 32.5,
            }
            service.create(data)  # Returns True
        """
        engine = create_engine_helper(data)

        truck = Truck(
            engine=engine,
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            kilometers=data["kilometers"],
            max_weight=data["max_weight"],
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = truck
        self.__last_index = last_index

        return True

    def delete(self, vehicle_id: int):
        """
        Delete a truck by its ID.

        Args:
            vehicle_id (int): ID of the truck to delete.

        Returns:
            None

        Example:
            service = TruckService()
            service.delete(1)
        """
        if vehicle_id not in self.__data:
            raise ValueError("Truck not found")
        del self.__data[vehicle_id]
