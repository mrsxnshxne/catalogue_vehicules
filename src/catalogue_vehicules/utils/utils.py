from catalogue_vehicules.core.interfaces.models.engine import Engine
from catalogue_vehicules.models.engines.diesel_engine import DieselEngine
from catalogue_vehicules.models.engines.electric_engine import ElectricEngine
from catalogue_vehicules.models.engines.gasoline_engine import GasolineEngine
from catalogue_vehicules.models.engines.hybrid_engine import HybridEngine


def create_engine_helper(data: dict) -> Engine:
    if data["engine_type"] == "hybrid":
        return HybridEngine(
            power_gasoline=data["engine_power_gasoline"],
            power_electric=data["engine_power_electric"],
            battery_capacity=data["engine_battery_capacity"],
            tank_capacity=data["engine_tank_capacity"],
            battery_consumption=data["engine_battery_consumption"],
            tank_consumption=data["engine_tank_consumption"]
        )
    elif data["engine_type"] == "electric":
        return ElectricEngine(
            power=data["engine_power"],
            battery_capacity=data["engine_capacity"],
            consumption=data["engine_consumption"]
        )
    elif data["engine_type"] == "gasoline":
        return GasolineEngine(
            power=data["engine_power"],
            tank_capacity=data["engine_capacity"],
            consumption=data["engine_consumption"]
        )
    elif data["engine_type"] == "diesel":
        return DieselEngine(
            power=data["engine_power"],
            tank_capacity=data["engine_capacity"],
            consumption=data["engine_consumption"]
        )
    else:
        raise ValueError("Engine type not supported")