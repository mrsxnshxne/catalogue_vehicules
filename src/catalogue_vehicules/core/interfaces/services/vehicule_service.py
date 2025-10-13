from abc import ABC, abstractmethod
from catalogue_vehicules.core.interfaces.models.vehicle import Vehicle

class VehicleService(ABC):
    @abstractmethod
    def get(self) -> list[Vehicle]:
        pass

    @abstractmethod
    def find(self, id: int) -> Vehicle:
        pass

    @abstractmethod
    def create(self, data: Vehicle):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass