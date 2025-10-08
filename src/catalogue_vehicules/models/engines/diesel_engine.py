from catalogue_vehicules.core.interfaces.engine import Engine


class DieselEngine(Engine):
    
    def __init__(self, power: int):
        super().__init__("diesel", power)
    
    def start_engine(self):
        print("Starting DieselEngine...")

    def stop_engine(self):
        print("Stopping DieselEngine...")