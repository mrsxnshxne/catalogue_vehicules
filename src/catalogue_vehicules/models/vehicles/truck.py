from catalogue_vehicules.core.interfaces.engine import Engine
from catalogue_vehicules.core.interfaces.vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self, engine: Engine, brand: str, model: str, year: int, empty_weight: float, max_weight: float):
        super().__init__(engine, brand, model, year)
        self.weight = empty_weight
        self.max_weight = empty_weight