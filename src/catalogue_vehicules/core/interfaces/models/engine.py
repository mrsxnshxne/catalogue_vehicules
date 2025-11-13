"""
Interface for Engine model
"""

from sqlalchemy import Column, Integer, String

from catalogue_vehicules.database.database import Base


class Engine(Base):
    __tablename__ = "engines"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    power = Column(Integer)

    tank_capacity = Column(Integer, nullable=True)
    tank_consumption = Column(Integer, nullable=True)

    battery_capacity = Column(Integer, nullable=True)
    battery_consumption = Column(Integer, nullable=True)