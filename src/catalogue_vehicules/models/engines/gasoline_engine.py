from catalogue_vehicules.core.interfaces.engine import Engine


class GasolineEngine(Engine):
    def start(self):
        print("Starting GasolineEngine...")

    def stop(self):
        print("Stopping GasolineEngine...")