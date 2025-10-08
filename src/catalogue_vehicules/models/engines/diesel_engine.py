from catalogue_vehicules.core.interfaces.engine import Engine


class DieselEngine(Engine):
    def start(self):
        print("Starting DieselEngine...")

    def stop(self):
        print("Stopping DieselEngine...")