"""
Moto service module
"""

from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle
from catalogue_vehicules.core.interfaces.services.vehicule_service import VehicleService
from catalogue_vehicules.models.vehicles.moto import Moto
from catalogue_vehicules.utils.utils import create_engine_helper
from catalogue_vehicules.utils.validators.moto_validator import validate_moto_data


class MotoService(VehicleService):
    def __init__(self):
        self.__last_index: int = 0
        self.__data: dict[int, Moto] = {}

    def get(self) -> list[Vehicle]:
        values = []
        for _, value in self.__data.items():
            values.append(value)
        return values

    def find(self, vehicle_id: int) -> Vehicle:
        if vehicle_id not in self.__data:
            raise ValueError("Moto not found")
        return self.__data[vehicle_id]

    @validate_moto_data
    def create(self, data: dict) -> bool:
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
        if vehicle_id not in self.__data:
            raise ValueError("Moto not found")
        del self.__data[vehicle_id]
