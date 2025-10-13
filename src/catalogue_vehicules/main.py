"""
Main module to demonstrate the functionality of the vehicle catalogue system.
"""

from catalogue_vehicules.services.car_service import CarService


def main():
    """
    Main function to demonstrate the functionality of the vehicle catalogue system.
    :rtype: None
    """
    car_service = CarService()
    car_service.create(
        {
            "brand": "Tesla",
            "model": "Model S",
            "year": 2021,
            "kilometers": 15000,
            "engine_type": "electric",
            "engine_power": 200,
            "engine_capacity": 100,
            "engine_consumption": 20,
            "trunk": 500,
        }
    )

    car_service.create(
        {
            "brand": "Toyota",
            "model": "Corolla",
            "year": 2019,
            "kilometers": 30000,
            "engine_type": "gasoline",
            "engine_power": 130,
            "engine_capacity": 50,
            "engine_consumption": 6,
            "trunk": 470,
        }
    )

    car_service.create(
        {
            "brand": "Ford",
            "model": "Focus",
            "year": 2018,
            "kilometers": 40000,
            "engine_type": "diesel",
            "engine_power": 120,
            "engine_capacity": 55,
            "engine_consumption": 5,
            "trunk": 375,
        }
    )

    car_service.create(
        {
            "brand": "Honda",
            "model": "CR-V Hybrid",
            "year": 2020,
            "kilometers": 25000,
            "engine_type": "hybrid",
            "engine_power_electric": 100,
            "engine_power_gasoline": 80,
            "engine_tank_capacity": 40,
            "engine_battery_capacity": 30,
            "engine_tank_consumption": 5,
            "engine_battery_consumption": 10,
            "trunk": 522,
        }
    )

    cars = car_service.get()
    for car in cars:
        print(car)

    car_service.delete(2)
    print("After deletion:")
    cars = car_service.get()
    for car in cars:
        print(car)

    car = car_service.find(1)
    print("Find car with ID 1:")
    print(car)


if __name__ == "__main__":
    main()
