"""
Service for managing car vehicles.
"""

from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle
from catalogue_vehicules.core.interfaces.services.vehicule_service import VehicleService
from catalogue_vehicules.models.vehicles.car import Car
from catalogue_vehicules.utils.utils import create_engine_helper
from catalogue_vehicules.utils.validators.car_validator import validate_car_data


class CarService(VehicleService):
    """
    Service class for managing cars in the vehicle catalogue.
    """

    def __init__(self):
        """
        Initialize the CarService with an empty data store and last index set to 0.

        Returns:
            None
        """
        self.__last_index: int = 0
        self.__data: dict[int, Car] = {}

    def get(self, engine: str | None = None) -> list[Vehicle]:
        """
        Get all cars in the catalogue.

        Args:
            engine (str | None): Engine type to filter by (optional).

        Returns:
            list[Vehicle]: List of all cars.

        Example:
            service = CarService()
            cars = service.get()
        """
        values = []
        for _, value in self.__data.items():
            if engine is None or value.engine.type == engine:
                values.append(value)
        return values

    def find(self, vehicle_id: int) -> Vehicle:
        """
        Find a car by its ID.

        Args:
            vehicle_id (int): ID of the car to find.

        Returns:
            Vehicle: The car with the given ID.

        Example:
            service = CarService()
            car = service.find(1)
        """
        if vehicle_id not in self.__data:
            raise ValueError("Car not found")
        return self.__data[vehicle_id]

    @validate_car_data
    def create(self, data: dict) -> bool:
        """
        Create a new car and add it to the catalogue.

        Args:
            data (dict): Data for the new car.

        Returns:
            bool: True if the car was created successfully.

        Example:
            service = CarService()
            car_data = {
                "brand": "Toyota",
                "model": "Corolla",
                "year": 2020,
                "kilometers": 15000,
                "trunk": 450,
                "engine_type": "gasoline",
                "engine_power": 132,
                "engine_capacity": 1800,
                "engine_consumption": 6.5,
            }
            service.create(car_data)  # Returns True
        """
        engine = create_engine_helper(data)

        car = Car(
            engine=engine,
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            kilometers=data["kilometers"],
            trunk=data["trunk"],
        )

        last_index = self.__last_index + 1
        self.__data[last_index] = car
        self.__last_index = last_index

        return True

    def delete(self, vehicle_id: int):
        """
        Delete a car by its ID.

        Args:
            vehicle_id (int): ID of the car to delete.

        Returns:
            None

        Example:
            service = CarService()
            service.delete(1)
        """
        if vehicle_id not in self.__data:
            raise ValueError("Car not found")
        del self.__data[vehicle_id]
