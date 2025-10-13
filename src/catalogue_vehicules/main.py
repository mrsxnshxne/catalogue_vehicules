from catalogue_vehicules.models.engines.diesel_engine import DieselEngine
from catalogue_vehicules.models.engines.electric_engine import ElectricEngine
from catalogue_vehicules.models.engines.gasoline_engine import GasolineEngine
from catalogue_vehicules.models.engines.hybrid_engine import HybridEngine
from catalogue_vehicules.models.vehicles.car import Car
from catalogue_vehicules.models.vehicles.moto import Moto
from catalogue_vehicules.models.vehicles.truck import Truck
from catalogue_vehicules.services.car_service import CarService


def main():
    # electric_engine = ElectricEngine(power=150, battery_capacity=75, consumption=15)
    # print(f"ElectricEngine Autonomy: {electric_engine.get_autonomy()} km")

    # gasoline_engine = GasolineEngine(power=150, tank_capacity=50, consumption=8)
    # print(f"GasolineEngine Autonomy: {gasoline_engine.get_autonomy()} km")
    #
    # diesel_engine = DieselEngine(power=150, tank_capacity=60, consumption=6)
    # print(f"DieselEngine Autonomy: {diesel_engine.get_autonomy()} km")
    #
    # hybrid_engine = HybridEngine(power_gasoline=100, power_electric=80, tank_capacity=40, battery_capacity=30, tank_consumption=5, battery_consumption=10)
    # print(f"HybridEngine Autonomy: {hybrid_engine.get_autonomy()} km")

    # car_vehicule = Car(engine=electric_engine, brand="Tesla", model="Model 3", year=2020, kilometers=20000, trunk=425)
    # print(f"Car Brand: {car_vehicule.brand}, Model: {car_vehicule.model}, Year: {car_vehicule.year}, Kilometers: {car_vehicule.kilometers}, Trunk: {car_vehicule.trunk}L, Engine: {car_vehicule.engine.type}")

    # moto_vehicule = Moto(engine=gasoline_engine, brand="Yamaha", model="MT-07", year=2019, kilometers=10000, license="A2")
    # print(f"Moto Brand: {moto_vehicule.brand}, Model: {moto_vehicule.model}, Year: {moto_vehicule.year}, Kilometers: {moto_vehicule.kilometers}, License: {moto_vehicule.license}, Engine: {moto_vehicule.engine.type}")
    #
    # truck_vehicule = Truck(engine=diesel_engine, brand="Volvo", model="FH16", year=2018, kilometers=50000, max_weight=44000)
    # print(f"Truck Brand: {truck_vehicule.brand}, Model: {truck_vehicule.model}, Year: {truck_vehicule.year}, Kilometers: {truck_vehicule.kilometers}, Max Weight: {truck_vehicule.max_weight}kg, Engine: {truck_vehicule.engine.type}")

    car_service = CarService()
    car_service.create({
        "brand": "Tesla",
        "model": "Model S",
        "year": 2021,
        "kilometers": 15000,
        "engine_type": "electric",
        "engine_power": 200,
        "engine_capacity": 100,
        "engine_consumption": 20,
        "trunk": 500
    })

    car_service.create({
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2019,
        "kilometers": 30000,
        "engine_type": "gasoline",
        "engine_power": 130,
        "engine_capacity": 50,
        "engine_consumption": 6,
        "trunk": 470
    })

    car_service.create({
        "brand": "Ford",
        "model": "Focus",
        "year": 2018,
        "kilometers": 40000,
        "engine_type": "diesel",
        "engine_power": 120,
        "engine_capacity": 55,
        "engine_consumption": 5,
        "trunk": 375
    })

    car_service.create({
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
        "trunk": 522
    })

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

if __name__ == '__main__':
    main()