from catalogue_vehicules.core.interfaces.engine import Engine


class ElectricEngine(Engine):
    def start(self):
        print("Starting ElectricEngine...")

    def stop(self):
        print("Stopping ElectricEngine...")