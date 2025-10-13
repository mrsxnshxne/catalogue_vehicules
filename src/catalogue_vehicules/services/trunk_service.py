from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle
from catalogue_vehicules.core.interfaces.services.vehicule_service import VehicleService
from catalogue_vehicules.models.vehicles.truck import Truck
from catalogue_vehicules.utils.utils import create_engine_helper
from catalogue_vehicules.utils.validators.truck_validator import validate_truck_data


class TruckService(VehicleService):

    def __init__(self):
        self.__last_index: int = 0
        self.__data: dict[int, Truck] = {}

    def get(self) -> list[Vehicle]:
        values = []
        for _, value in self.__data.items():
            values.append(value)
        return values

    def find(self, id: int) -> Vehicle:
        if not id in self.__data:
            raise ValueError("Truck not found")
        return self.__data[id]

    @validate_truck_data
    def create(self, data: dict):
        engine = create_engine_helper(data)

        truck = Truck(
            engine=engine,
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            kilometers=data["kilometers"],
            max_weight=data["max_weight"]
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = truck
        self.__last_index = last_index

    def delete(self, id: int):
        if not id in self.__data:
            raise ValueError("Moto not found")
        del self.__data[id]