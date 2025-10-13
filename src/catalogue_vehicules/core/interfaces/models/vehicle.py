"""
Interface for Vehicle model
"""

from abc import ABC, abstractmethod
from catalogue_vehicules.core.interfaces.models.engine import Engine


class Vehicle(ABC):
    """
    Interface for Vehicle model
    """

    @property
    @abstractmethod
    def engine(self) -> Engine:
        """
        Get the engine of the vehicle
        :return: Engine
        """
        pass

    @engine.setter
    @abstractmethod
    def engine(self, engine: Engine):
        """
        Set the engine of the vehicle
        :param engine:
        :return:
        """
        pass

    @property
    @abstractmethod
    def brand(self) -> str:
        """
        Get the brand of the vehicle
        :return: str
        """
        pass

    @brand.setter
    @abstractmethod
    def brand(self, brand: str):
        """
        Set the brand of the vehicle
        :param brand:
        :return:
        """
        pass

    @property
    @abstractmethod
    def model(self) -> str:
        """
        Get the model of the vehicle
        :return: str
        """
        pass

    @model.setter
    @abstractmethod
    def model(self, model: str):
        """
        Set the model of the vehicle
        :param model:
        :return:
        """
        pass

    @property
    @abstractmethod
    def year(self) -> int:
        """
        Get the year of the vehicle
        :return: int
        """
        pass

    @year.setter
    @abstractmethod
    def year(self, year: int):
        """
        Set the year of the vehicle
        :param year:
        :return:
        """
        pass

    @property
    @abstractmethod
    def kilometers(self) -> float:
        """
        Get the kilometers of the vehicle
        :return: float
        """
        pass

    @kilometers.setter
    @abstractmethod
    def kilometers(self, kilometers: float):
        """
        Set the kilometers of the vehicle
        :param kilometers:
        :return:
        """
        pass
