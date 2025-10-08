from catalogue_vehicules.core.interfaces.engine import Engine


class HybridEngine(Engine):

    def __init__(self, power: int):
        super().__init__("hybrid", power)

    def start_engine(self):
        print("Starting HybridEngine...")

    def stop_engine(self):
        print("Stopping HybridEngine...")