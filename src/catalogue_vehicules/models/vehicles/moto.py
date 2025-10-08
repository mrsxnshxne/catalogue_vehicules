from catalogue_vehicules.core.interfaces.engine import Engine
from catalogue_vehicules.core.interfaces.vehicle import Vehicle


class Moto(Vehicle):

    def __init__(self, engine: Engine, brand: str, model: str, year: int, license_type: str):
        super().__init__(engine, brand, model, year)
        self.license_type = license_type