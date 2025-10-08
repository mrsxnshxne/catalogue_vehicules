from catalogue_vehicules.core.interfaces.engine import Engine
from catalogue_vehicules.core.interfaces.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, engine: Engine, brand: str, model: str, year: int, storage: int, category: str):
        super().__init__(engine, brand, model, year)
        self.storage = storage
        self.category = category