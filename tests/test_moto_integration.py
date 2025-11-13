"""
Integration tests for the MotoService class.
"""

import pytest

from catalogue_vehicules.services.vehicle.moto_service import MotoService


def test_diesel_moto_creation():
    """
    Test the creation of a diesel moto with valid data.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Yamaha",
        "model": "MT-07",
        "year": 2022,
        "kilometers": 5000,
        "license": 125,
        "engine_type": "diesel",
        "engine_power": 75,
        "engine_capacity": 689,
        "engine_consumption": 4.5,
    }
    assert service.create(data) is True


def test_gasoline_moto_creation():
    """
    Test the creation of a gasoline moto with valid data.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Honda",
        "model": "CBR600RR",
        "year": 2021,
        "kilometers": 8000,
        "license": 600,
        "engine_type": "gasoline",
        "engine_power": 120,
        "engine_capacity": 599,
        "engine_consumption": 5.2,
    }
    assert service.create(data) is True


def test_electric_moto_creation():
    """
    Test the creation of an electric moto with valid data.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Zero",
        "model": "SR/F",
        "year": 2023,
        "kilometers": 2000,
        "license": 125,
        "engine_type": "electric",
        "engine_power": 110,
        "engine_capacity": 14400,
        "engine_consumption": 15.5,
    }
    assert service.create(data) is True


def test_hybrid_moto_creation():
    """
    Test the creation of a hybrid moto with valid data.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "BMW",
        "model": "CE 04",
        "year": 2023,
        "kilometers": 1000,
        "license": 400,
        "engine_type": "hybrid",
        "engine_power_electric": 42,
        "engine_battery_capacity": 8900,
        "engine_battery_consumption": 12.0,
        "engine_power_gasoline": 25,
        "engine_tank_capacity": 5,
        "engine_tank_consumption": 3.5,
    }
    assert service.create(data) is True


def test_moto_creation_type_fail():
    """
    Test the creation of a moto with invalid data type.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Yamaha",
        "model": "MT-07",
        "year": 2022,
        "kilometers": "5000",  # Error here, should be int
        "license": 125,
        "engine_type": "diesel",
        "engine_power": 75,
        "engine_capacity": 689,
        "engine_consumption": 4.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'kilometers' doit être de type" in str(excinfo.value)


def test_moto_creation_missing_value_fail():
    """
    Test the creation of a moto with missing required field.
    :rtype: None
    """
    service = MotoService()
    data = {
        # "brand": "Yamaha",  # Error here, missing field
        "model": "MT-07",
        "year": 2022,
        "kilometers": 5000,
        "license": 125,
        "engine_type": "diesel",
        "engine_power": 75,
        "engine_capacity": 689,
        "engine_consumption": 4.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'brand' est obligatoire." in str(excinfo.value)


def test_moto_creation_invalid_engine_type_fail():
    """
    Test the creation of a moto with invalid engine type.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Yamaha",
        "model": "MT-07",
        "year": 2022,
        "kilometers": 5000,
        "license": 125,
        "engine_type": "nuclear",  # Invalid engine type
        "engine_power": 75,
        "engine_capacity": 689,
        "engine_consumption": 4.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Type de moteur invalide" in str(excinfo.value)


def test_hybrid_moto_missing_gasoline_power_fail():
    """
    Test the creation of a hybrid moto with missing gasoline power field.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "BMW",
        "model": "CE 04",
        "year": 2023,
        "kilometers": 1000,
        "license": 400,
        "engine_type": "hybrid",
        "engine_power_electric": 42,
        "engine_battery_capacity": 8900,
        "engine_battery_consumption": 12.0,
        # "engine_power_gasoline": 25,  # Missing required field
        "engine_tank_capacity": 5,
        "engine_tank_consumption": 3.5,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'engine_power_gasoline' est obligatoire pour un véhicule hybride." in str(excinfo.value)


def test_moto_get_success():
    """
    Test the retrieval of all motos after creating a moto.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Yamaha",
        "model": "MT-07",
        "year": 2022,
        "kilometers": 5000,
        "license": 125,
        "engine_type": "diesel",
        "engine_power": 75,
        "engine_capacity": 689,
        "engine_consumption": 4.5,
    }
    service.create(data)
    motos = service.get()
    assert len(motos) == 1
    assert motos[0].brand == "Yamaha"
    assert motos[0].model == "MT-07"
    assert motos[0].license == 125


def test_moto_find_success():
    """
    Test the retrieval of a moto by ID after creating a moto.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Honda",
        "model": "CBR600RR",
        "year": 2021,
        "kilometers": 8000,
        "license": 600,
        "engine_type": "gasoline",
        "engine_power": 120,
        "engine_capacity": 599,
        "engine_consumption": 5.2,
    }
    service.create(data)
    moto = service.find(1)
    assert moto.brand == "Honda"
    assert moto.model == "CBR600RR"
    assert moto.license == 600


def test_moto_find_fail():
    """
    Test the retrieval of a moto by ID that does not exist.
    :rtype: None
    """
    service = MotoService()
    with pytest.raises(ValueError) as excinfo:
        service.find(1)
    assert "Moto not found" in str(excinfo.value)


def test_moto_delete_success():
    """
    Test the deletion of a moto by ID after creating a moto.
    :rtype: None
    """
    service = MotoService()
    data = {
        "brand": "Zero",
        "model": "SR/F",
        "year": 2023,
        "kilometers": 2000,
        "license": 125,
        "engine_type": "electric",
        "engine_power": 110,
        "engine_capacity": 14400,
        "engine_consumption": 15.5,
    }
    service.create(data)
    service.delete(1)
    motos = service.get()
    assert len(motos) == 0


def test_moto_delete_fail():
    """
    Test the deletion of a moto by ID that does not exist.
    :rtype: None
    """
    service = MotoService()
    with pytest.raises(ValueError) as excinfo:
        service.delete(1)
    assert "Moto not found" in str(excinfo.value)
