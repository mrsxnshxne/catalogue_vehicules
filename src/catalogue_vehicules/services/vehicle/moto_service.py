"""
Moto service module
"""

from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle
from catalogue_vehicules.core.interfaces.services.vehicule_service import VehicleService
from catalogue_vehicules.models.vehicles.moto import Moto
from catalogue_vehicules.utils.utils import create_engine_helper
from catalogue_vehicules.utils.validators.moto_validator import validate_moto_data


class MotoService(VehicleService):
    """
    Service class for managing motos in the vehicle catalogue.
    """

    def __init__(self):
        """
        Initialize the MotoService with an empty data store and last index set to 0.
        """
        self.__last_index: int = 0
        self.__data: dict[int, Moto] = {}

    def get(self,  engine: str | None = None) -> list[Vehicle]:
        """
        Get all motos in the catalogue.

        Returns:
            list[Vehicle]: List of all motos.
        """
        values = []
        for _, value in self.__data.items():
            if engine is None or value.engine.type == engine:
                values.append(value)
        return values

    def find(self, vehicle_id: int) -> Vehicle:
        """
        Find a moto by its ID.

        Args:
            vehicle_id (int): ID of the moto to find.

        Returns:
            Vehicle: The moto with the given ID.

        Example:
            service = MotoService()
            moto = service.find(1)
        """
        if vehicle_id not in self.__data:
            raise ValueError("Moto not found")
        return self.__data[vehicle_id]

    @validate_moto_data
    def create(self, data: dict) -> bool:
        """
        Create a new moto and add it to the catalogue.

        Args:
            data (dict): Data for the new moto.

        Returns:
            bool: True if the moto was created successfully.

        Example:
            service = MotoService()
            data = {
                "brand": "Yamaha",
                "model": "MT-07",
                "year": 2022,
                "kilometers": 5000,
                "license": 125,
                "engine_type": "diesel",
                "engine_power": 75,
                "engine_capacity": 689,
                "engine_consumption": 4.5,
            }
            service.create(data)  # Returns: True
        """
        engine = create_engine_helper(data)

        moto = Moto(
            engine=engine,
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            kilometers=data["kilometers"],
            license_type=data["license"],
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = moto
        self.__last_index = last_index

        return True

    def delete(self, vehicle_id: int):
        """
        Delete a moto by its ID.

        Args:
            vehicle_id (int): ID of the moto to delete.

        Returns:
            None

        Example:
            service = MotoService()
            service.delete(1)
        """
        if vehicle_id not in self.__data:
            raise ValueError("Moto not found")
        del self.__data[vehicle_id]
