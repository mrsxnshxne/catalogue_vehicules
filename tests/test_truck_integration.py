"""
Integration tests for the TruckService class.
"""

import pytest

from catalogue_vehicules.services.vehicle.trunk_service import TruckService


def test_diesel_truck_creation():
    """
    Test the creation of a diesel truck with valid data.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Volvo",
        "model": "FH16",
        "year": 2021,
        "kilometers": 120000,
        "max_weight": 40000,
        "engine_type": "diesel",
        "engine_power": 520,
        "engine_capacity": 13000,
        "engine_consumption": 32.5,
    }
    assert service.create(data) is True


def test_gasoline_truck_creation():
    """
    Test the creation of a gasoline truck with valid data.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Ford",
        "model": "F-150",
        "year": 2022,
        "kilometers": 50000,
        "max_weight": 3500,
        "engine_type": "gasoline",
        "engine_power": 400,
        "engine_capacity": 5000,
        "engine_consumption": 15.2,
    }
    assert service.create(data) is True


def test_electric_truck_creation():
    """
    Test the creation of an electric truck with valid data.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Tesla",
        "model": "Semi",
        "year": 2023,
        "kilometers": 10000,
        "max_weight": 36000,
        "engine_type": "electric",
        "engine_power": 1000,
        "engine_capacity": 500000,
        "engine_consumption": 120.0,
    }
    assert service.create(data) is True


def test_hybrid_truck_creation():
    """
    Test the creation of a hybrid truck with valid data.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Mercedes",
        "model": "eActros",
        "year": 2023,
        "kilometers": 25000,
        "max_weight": 26000,
        "engine_type": "hybrid",
        "engine_power_electric": 330,
        "engine_battery_capacity": 420000,
        "engine_battery_consumption": 85.0,
        "engine_power_gasoline": 280,
        "engine_tank_capacity": 200,
        "engine_tank_consumption": 28.5,
    }
    assert service.create(data) is True


def test_truck_creation_type_fail():
    """
    Test the creation of a truck with invalid data type.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Volvo",
        "model": "FH16",
        "year": 2021,
        "kilometers": "120000",  # Error here, should be int
        "max_weight": 40000,
        "engine_type": "diesel",
        "engine_power": 520,
        "engine_capacity": 13000,
        "engine_consumption": 32.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'kilometers' doit être de type" in str(excinfo.value)


def test_truck_creation_missing_value_fail():
    """
    Test the creation of a truck with missing required field.
    :rtype: None
    """
    service = TruckService()
    data = {
        # "brand": "Volvo",  # Error here, missing field
        "model": "FH16",
        "year": 2021,
        "kilometers": 120000,
        "max_weight": 40000,
        "engine_type": "diesel",
        "engine_power": 520,
        "engine_capacity": 13000,
        "engine_consumption": 32.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'brand' est obligatoire." in str(excinfo.value)


def test_truck_creation_missing_max_weight_fail():
    """
    Test the creation of a truck with missing max_weight field.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Volvo",
        "model": "FH16",
        "year": 2021,
        "kilometers": 120000,
        # "max_weight": 40000,  # Error here, missing field specific to trucks
        "engine_type": "diesel",
        "engine_power": 520,
        "engine_capacity": 13000,
        "engine_consumption": 32.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'max_weight' est obligatoire." in str(excinfo.value)


def test_truck_creation_invalid_engine_type_fail():
    """
    Test the creation of a truck with invalid engine type.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Volvo",
        "model": "FH16",
        "year": 2021,
        "kilometers": 120000,
        "max_weight": 40000,
        "engine_type": "steam",  # Invalid engine type
        "engine_power": 520,
        "engine_capacity": 13000,
        "engine_consumption": 32.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Type de moteur invalide" in str(excinfo.value)


def test_hybrid_truck_missing_electric_power_fail():
    """
    Test the creation of a hybrid truck with missing electric power field.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Mercedes",
        "model": "eActros",
        "year": 2023,
        "kilometers": 25000,
        "max_weight": 26000,
        "engine_type": "hybrid",
        # "engine_power_electric": 330,  # Missing required field
        "engine_battery_capacity": 420000,
        "engine_battery_consumption": 85.0,
        "engine_power_gasoline": 280,
        "engine_tank_capacity": 200,
        "engine_tank_consumption": 28.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'engine_power_electric' est obligatoire pour un véhicule hybride." in str(excinfo.value)


def test_electric_truck_missing_capacity_fail():
    """
    Test the creation of an electric truck with missing capacity field.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Tesla",
        "model": "Semi",
        "year": 2023,
        "kilometers": 10000,
        "max_weight": 36000,
        "engine_type": "electric",
        "engine_power": 1000,
        # "engine_capacity": 500000,  # Missing required field
        "engine_consumption": 120.0,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'engine_capacity' est obligatoire pour un véhicule electrique." in str(excinfo.value)


def test_truck_get_success():
    """
    Test the retrieval of all trucks after creating a truck.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Volvo",
        "model": "FH16",
        "year": 2021,
        "kilometers": 120000,
        "max_weight": 40000,
        "engine_type": "diesel",
        "engine_power": 520,
        "engine_capacity": 13000,
        "engine_consumption": 32.5,
    }
    service.create(data)
    trucks = service.get()
    assert len(trucks) == 1
    assert trucks[0].brand == "Volvo"
    assert trucks[0].model == "FH16"
    assert trucks[0].max_weight == 40000


def test_truck_find_success():
    """
    Test the retrieval of a truck by ID after creating a truck.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Ford",
        "model": "F-150",
        "year": 2022,
        "kilometers": 50000,
        "max_weight": 3500,
        "engine_type": "gasoline",
        "engine_power": 400,
        "engine_capacity": 5000,
        "engine_consumption": 15.2,
    }
    service.create(data)
    truck = service.find(1)
    assert truck.brand == "Ford"
    assert truck.model == "F-150"
    assert truck.max_weight == 3500


def test_truck_find_fail():
    """
    Test the retrieval of a truck by ID that does not exist.
    :rtype: None
    """
    service = TruckService()
    with pytest.raises(ValueError) as excinfo:
        service.find(1)
    assert "Truck not found" in str(excinfo.value)


def test_truck_delete_success():
    """
    Test the deletion of a truck by ID after creating a truck.
    :rtype: None
    """
    service = TruckService()
    data = {
        "brand": "Tesla",
        "model": "Semi",
        "year": 2023,
        "kilometers": 10000,
        "max_weight": 36000,
        "engine_type": "electric",
        "engine_power": 1000,
        "engine_capacity": 500000,
        "engine_consumption": 120.0,
    }
    service.create(data)
    service.delete(1)
    trucks = service.get()
    assert len(trucks) == 0


def test_truck_delete_fail():
    """
    Test the deletion of a truck by ID that does not exist.
    :rtype: None
    """
    service = TruckService()
    with pytest.raises(ValueError) as excinfo:
        service.delete(1)
    assert "Truck not found" in str(excinfo.value)
