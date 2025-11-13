"""
Interface for Engine service
"""

from abc import ABC, abstractmethod
from catalogue_vehicules.core.interfaces.models.engine import Engine


class EngineService(ABC):
    """
    Interface for Engine service
    """

    @abstractmethod
    def get(self) -> list[Engine]:
        """
        Get all engines
        :return:
        """
        pass

    @abstractmethod
    def find(self, engine_id: int) -> Engine:
        """
        Find an engine by its ID
        :param engine_id:
        :return:
        """
        pass

    @abstractmethod
    def create(self, data: Engine):
        """
        Create a new engine
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def delete(self, engine_id: int):
        """
        Delete an engine by its ID
        :param engine_id:
        :return:
        """
        pass
