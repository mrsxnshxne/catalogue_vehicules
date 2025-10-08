from catalogue_vehicules.core.interfaces.engine import Engine


class ElectricEngine(Engine):

    def __init__(self, power: int):
        super().__init__("electric", power)

    def start_engine(self):
        print("Starting ElectricEngine...")

    def stop_engine(self):
        print("Stopping ElectricEngine...")