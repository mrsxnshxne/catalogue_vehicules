from fastapi import APIRouter

from catalogue_vehicules.schemas.vehicule import VehicleSchema
from catalogue_vehicules.services.vehicle.car_service import CarService
from catalogue_vehicules.services.vehicle.moto_service import MotoService
from catalogue_vehicules.services.vehicle.trunk_service import TruckService


vehicleRouter = APIRouter(prefix="/vehicles", tags=["vehicles"])


@vehicleRouter.get("/")
async def list_vehicles(
        type: str | None = None,
        engine: str | None = None
):
    carService = CarService()
    motoService = MotoService()
    truckService = TruckService()

    if type == "car":
        cars = carService.get(engine)
        return cars
    elif type == "moto":
        motos = motoService.get(engine)
        return motos
    elif type == "truck":
        trucks = truckService.get(engine)
        return trucks
    else:
        cars = carService.get(engine)
        motos = motoService.get(engine)
        trucks = truckService.get(engine)
        return {
            "cars": cars,
            "motos": motos,
            "trucks": trucks
        }


@vehicleRouter.get("/{id}")
async def get_vehicle(id: int):
    service = CarService()
    car = service.find(id)
    return car


@vehicleRouter.post("/")
async def create_vehicle(vehicle: VehicleSchema):
    if vehicle.type == "car":
        service = CarService()
        service.create({
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "kilometers": vehicle.kilometers,
            "trunk": vehicle.trunk,

            "engine_id": vehicle.engine_id,
        })
        return { "message": "Car created successfully" }

    elif vehicle.type == "moto":
        service = MotoService()
        service.create({
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "kilometers": vehicle.kilometers,
            "license": vehicle.license,

            "engine_id": vehicle.engine_id,
        })
        return { "message": "Moto created successfully" }

    elif vehicle.type == "truck":
        service = TruckService()
        service.create({
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "kilometers": vehicle.kilometers,
            "max_weight": vehicle.max_weight,

            "engine_id": vehicle.engine_id,
        })
        return { "message": "Truck created successfully" }

    else:
        return {"error": "Invalid vehicle type"}


@vehicleRouter.delete("/{id}")
async def delete_vehicle(id: int):
    service = CarService()
    service.delete(id)
    return { "message": "Car deleted successfully" }