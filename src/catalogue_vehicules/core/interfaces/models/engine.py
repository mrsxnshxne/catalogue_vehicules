"""
Interface for Engine model
"""

from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Interface for Engine model
    """

    @property
    @abstractmethod
    def type(self) -> str:
        """
        Get the type of the engine
        :return: str
        """
        pass

    @property
    @abstractmethod
    def power(self) -> int:
        """
        Get the power of the engine
        :return:
        """
        pass

    @power.setter
    @abstractmethod
    def power(self, power: int):
        """
        Set the power of the engine
        :param power:
        :return:
        """
        pass

    @abstractmethod
    def get_autonomy(self) -> float:
        """
        Get the autonomy of the engine
        :return: float
        """
        pass
