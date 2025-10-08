from abc import ABC

from catalogue_vehicules.core.interfaces.engine import Engine


class HybridEngine(Engine):
    def start(self):
        print("Starting HybridEngine...")

    def stop(self):
        print("Stopping HybridEngine...")