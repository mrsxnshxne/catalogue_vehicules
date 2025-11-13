"""
Interface for Vehicle service
"""

from abc import ABC, abstractmethod
from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle


class VehicleService(ABC):
    """
    Interface for Vehicle service
    """

    @abstractmethod
    def get(self, engine: str | None = None) -> list[Vehicle]:
        """
        Get all vehicles
        :return:
        """
        pass

    @abstractmethod
    def find(self, vehicle_id: int) -> Vehicle:
        """
        Find a vehicle by its ID
        :param vehicle_id:
        :return:
        """
        pass

    @abstractmethod
    def create(self, data: Vehicle):
        """
        Create a new vehicle
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def delete(self, vehicle_id: int):
        """
        Delete a vehicle by its ID
        :param vehicle_id:
        :return:
        """
        pass
