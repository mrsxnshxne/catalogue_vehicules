"""
Integration tests for the CarService class.
"""

import pytest

from catalogue_vehicules.services.vehicle.car_service import CarService


def test_diesel_car_creation():
    """
    Test the creation of a diesel car with valid data.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        "trunk": 450,
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }
    assert service.create(data) is True


def test_gasoline_car_creation():
    """
    Test the creation of a gasoline car with valid data.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Honda",
        "model": "Civic",
        "year": 2022,
        "kilometers": 25000,
        "trunk": 428,
        "engine_type": "gasoline",
        "engine_power": 158,
        "engine_capacity": 2000,
        "engine_consumption": 6.8,
    }
    assert service.create(data) is True


def test_electric_car_creation():
    """
    Test the creation of an electric car with valid data.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Tesla",
        "model": "Model 3",
        "year": 2023,
        "kilometers": 5000,
        "trunk": 425,
        "engine_type": "electric",
        "engine_power": 283,
        "engine_capacity": 75000,
        "engine_consumption": 15.0,
    }
    assert service.create(data) is True


def test_hybrid_car_creation():
    """
    Test the creation of a hybrid car with valid data.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Prius",
        "year": 2023,
        "kilometers": 8000,
        "trunk": 502,
        "engine_type": "hybrid",
        "engine_power_electric": 95,
        "engine_battery_capacity": 8800,
        "engine_battery_consumption": 4.5,
        "engine_power_gasoline": 98,
        "engine_tank_capacity": 43,
        "engine_tank_consumption": 3.9,
    }
    assert service.create(data) is True


def test_car_creation_type_fail():
    """
    Test the creation of a car with invalid data type.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": "15000",  # Error here, should be int
        "trunk": 450,
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'kilometers' doit être de type" in str(excinfo.value)


def test_car_creation_missing_value_fail():
    """
    Test the creation of a car with missing required field.
    :rtype: None
    """
    service = CarService()
    data = {
        # "brand": "Toyota",  # Error here, missing field
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        "trunk": 450,
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'brand' est obligatoire." in str(excinfo.value)


def test_car_creation_missing_trunk_fail():
    """
    Test the creation of a car with missing trunk field (specific to cars).
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        # "trunk": 450,  # Error here, missing field specific to cars
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'trunk' est obligatoire." in str(excinfo.value)


def test_car_creation_invalid_engine_type_fail():
    """
    Test the creation of a car with invalid engine type.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        "trunk": 450,
        "engine_type": "nuclear",  # Invalid engine type
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Type de moteur invalide" in str(excinfo.value)


def test_hybrid_car_missing_gasoline_power_fail():
    """
    Test the creation of a hybrid car with missing gasoline power field.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Prius",
        "year": 2023,
        "kilometers": 8000,
        "trunk": 502,
        "engine_type": "hybrid",
        "engine_power_electric": 95,
        "engine_battery_capacity": 8800,
        "engine_battery_consumption": 4.5,
        # "engine_power_gasoline": 98,  # Missing required field
        "engine_tank_capacity": 43,
        "engine_tank_consumption": 3.9,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'engine_power_gasoline' est obligatoire pour un véhicule hybride." in str(excinfo.value)


def test_electric_car_missing_consumption_fail():
    """
    Test the creation of an electric car with missing consumption field.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Tesla",
        "model": "Model 3",
        "year": 2023,
        "kilometers": 5000,
        "trunk": 425,
        "engine_type": "electric",
        "engine_power": 283,
        "engine_capacity": 75000,
        # "engine_consumption": 15.0,  # Missing required field
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'engine_consumption' est obligatoire pour un véhicule electrique." in str(excinfo.value)


def test_diesel_car_missing_engine_power_fail():
    """
    Test the creation of a diesel car with missing engine power field.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        "trunk": 450,
        "engine_type": "diesel",
        # "engine_power": 120,  # Missing required field for thermic engines
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }

    with pytest.raises(ValueError) as excinfo:
        service.create(data)

    assert "Le champ 'engine_power' est obligatoire pour un véhicule thermique." in str(excinfo.value)


def test_car_get_success():
    """
    Test the retrieval of all cars after creating a car.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        "trunk": 450,
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }
    service.create(data)
    cars = service.get()
    assert len(cars) == 1
    assert cars[0].brand == "Toyota"
    assert cars[0].model == "Corolla"
    assert cars[0].trunk == 450


def test_car_get_multiple_success():
    """
    Test the retrieval of multiple cars after creating several cars.
    :rtype: None
    """
    service = CarService()

    # Create first car
    data1 = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        "trunk": 450,
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }
    service.create(data1)

    # Create second car
    data2 = {
        "brand": "Honda",
        "model": "Civic",
        "year": 2022,
        "kilometers": 25000,
        "trunk": 428,
        "engine_type": "gasoline",
        "engine_power": 158,
        "engine_capacity": 2000,
        "engine_consumption": 6.8,
    }
    service.create(data2)

    cars = service.get()
    assert len(cars) == 2
    brands = [car.brand for car in cars]
    assert "Toyota" in brands
    assert "Honda" in brands


def test_car_find_success():
    """
    Test the retrieval of a car by ID after creating a car.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Honda",
        "model": "Civic",
        "year": 2022,
        "kilometers": 25000,
        "trunk": 428,
        "engine_type": "gasoline",
        "engine_power": 158,
        "engine_capacity": 2000,
        "engine_consumption": 6.8,
    }
    service.create(data)
    car = service.find(1)
    assert car.brand == "Honda"
    assert car.model == "Civic"
    assert car.trunk == 428


def test_car_find_fail():
    """
    Test the retrieval of a car by ID that does not exist.
    :rtype: None
    """
    service = CarService()
    with pytest.raises(ValueError) as excinfo:
        service.find(1)
    assert "Car not found" in str(excinfo.value)


def test_car_delete_success():
    """
    Test the deletion of a car by ID after creating a car.
    :rtype: None
    """
    service = CarService()
    data = {
        "brand": "Tesla",
        "model": "Model 3",
        "year": 2023,
        "kilometers": 5000,
        "trunk": 425,
        "engine_type": "electric",
        "engine_power": 283,
        "engine_capacity": 75000,
        "engine_consumption": 15.0,
    }
    service.create(data)
    service.delete(1)
    cars = service.get()
    assert len(cars) == 0


def test_car_delete_fail():
    """
    Test the deletion of a car by ID that does not exist.
    :rtype: None
    """
    service = CarService()
    with pytest.raises(ValueError) as excinfo:
        service.delete(1)
    assert "Car not found" in str(excinfo.value)


def test_car_delete_from_multiple_success():
    """
    Test the deletion of one car when multiple cars exist.
    :rtype: None
    """
    service = CarService()

    # Create first car
    data1 = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "kilometers": 15000,
        "trunk": 450,
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 1800,
        "engine_consumption": 5.2,
    }
    service.create(data1)

    # Create second car
    data2 = {
        "brand": "Honda",
        "model": "Civic",
        "year": 2022,
        "kilometers": 25000,
        "trunk": 428,
        "engine_type": "gasoline",
        "engine_power": 158,
        "engine_capacity": 2000,
        "engine_consumption": 6.8,
    }
    service.create(data2)

    # Delete first car
    service.delete(1)
    cars = service.get()
    assert len(cars) == 1
    assert cars[0].brand == "Honda"
