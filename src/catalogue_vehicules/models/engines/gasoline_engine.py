from catalogue_vehicules.core.interfaces.engine import Engine


class GasolineEngine(Engine):

    def __init__(self, power: int):
        super().__init__("gazoline", power)

    def start_engine(self):
        print("Starting GasolineEngine...")

    def stop_engine(self):
        print("Stopping GasolineEngine...")