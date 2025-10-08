from catalogue_vehicules.models.engines.diesel_engine import DieselEngine
from catalogue_vehicules.models.engines.electric_engine import ElectricEngine
from catalogue_vehicules.models.engines.gasoline_engine import GasolineEngine
from catalogue_vehicules.models.engines.hybrid_engine import HybridEngine


def main():
    electric_engine = ElectricEngine(power=150, battery_capacity=75, consumption=15)
    print(f"ElectricEngine Autonomy: {electric_engine.get_autonomy()} km")

    gasoline_engine = GasolineEngine(power=150, tank_capacity=50, consumption=8)
    print(f"GasolineEngine Autonomy: {gasoline_engine.get_autonomy()} km")

    diesel_engine = DieselEngine(power=150, tank_capacity=60, consumption=6)
    print(f"DieselEngine Autonomy: {diesel_engine.get_autonomy()} km")

    hybrid_engine = HybridEngine(power_gasoline=100, power_electric=80, tank_capacity=40, battery_capacity=30, tank_consumption=5, battery_consumption=10)
    print(f"HybridEngine Autonomy: {hybrid_engine.get_autonomy()} km")

if __name__ == '__main__':
    main()