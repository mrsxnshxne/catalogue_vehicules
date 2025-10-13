from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle
from catalogue_vehicules.core.interfaces.services.vehicule_service import VehicleService
from catalogue_vehicules.models.vehicles.car import Car
from catalogue_vehicules.utils.utils import create_engine_helper
from catalogue_vehicules.utils.validators.car_validator import validate_car_data


class CarService(VehicleService):

    def __init__(self):
        self.__last_index: int = 0
        self.__data: dict[int, Car] = {}

    def get(self) -> list[Vehicle]:
        values = []
        for _, value in self.__data.items():
            values.append(value)
        return values

    def find(self, id: int) -> Vehicle:
        if not id in self.__data:
            raise ValueError("Car not found")
        return self.__data[id]

    @validate_car_data
    def create(self, data: dict):
        engine = create_engine_helper(data)

        car = Car(
            engine=engine,
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            kilometers=data["kilometers"],
            trunk=data["trunk"]
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = car
        self.__last_index = last_index

    def delete(self, id: int):
        if not id in self.__data:
            raise ValueError("Car not found")
        del self.__data[id]