"""
Interface for Vehicle model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from catalogue_vehicules.core.interfaces.models.engine import Engine
from catalogue_vehicules.database.database import Base


class Vehicle(Base):
    """
    Vehicle interface
    """

    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    kilometers = Column(Integer, nullable=False)

    trunk = Column(Integer, nullable=True)
    license_type = Column(String, nullable=True)
    max_weight = Column(Integer, nullable=True)

    engine_id = Column(Integer, ForeignKey("engines.id"))
    engine = relationship("Engine", backref="vehicles")
