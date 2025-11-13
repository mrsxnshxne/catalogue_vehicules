"""
Unit tests for the engine models.
"""
import pytest

from catalogue_vehicules.models.engines.diesel_engine import DieselEngine
from catalogue_vehicules.models.engines.electric_engine import ElectricEngine
from catalogue_vehicules.models.engines.hybrid_engine import HybridEngine
from catalogue_vehicules.utils.utils import create_engine_helper


def test_get_autonomy_electric():
    """
    Test the get_autonomy method of the ElectricEngine class.
    :rtype: None
    """
    battery = 60
    power = 160
    consumption = 5

    engine_electric = ElectricEngine(
        power=power, battery_capacity=battery, consumption=consumption
    )
    autonomy_theory = battery / consumption * 100
    autonomy = engine_electric.get_autonomy()

    assert autonomy == autonomy_theory


def test_get_autonomy_diesel():
    """
    Test the get_autonomy method of the DieselEngine class.
    :rtype: None
    """
    tank = 60
    power = 160
    consumption = 5

    engine_diesel = DieselEngine(
        power=power, tank_capacity=tank, consumption=consumption
    )
    autonomy_theory = tank / consumption * 100
    autonomy = engine_diesel.get_autonomy()

    assert autonomy == autonomy_theory


def test_get_autonomy_hybrid():
    """
    Test the get_autonomy method of the HybridEngine class.
    :rtype: None
    """
    tank = 40
    battery = 30
    power_gasoline = 100
    power_electric = 80
    tank_consumption = 5
    battery_consumption = 10

    engine_hybrid = HybridEngine(
        power_gasoline=power_gasoline,
        power_electric=power_electric,
        tank_capacity=tank,
        battery_capacity=battery,
        tank_consumption=tank_consumption,
        battery_consumption=battery_consumption,
    )
    autonomy_theory = (tank / tank_consumption * 100) + (
        battery / battery_consumption * 100
    )
    autonomy = engine_hybrid.get_autonomy()

    assert autonomy == autonomy_theory

def test_engine_creation_with_bad_type_error():
    """
    Test the creation of an engine with an unsupported type.
    :return:
    """
    with pytest.raises(ValueError) as excinfo:
        create_engine_helper({
            "engine_type": "unknown",
            "engine_power": 160,
            "engine_capacity": 2000,
            "engine_consumption": 5.0,
        })

    assert "Engine type not supported" in str(excinfo.value)