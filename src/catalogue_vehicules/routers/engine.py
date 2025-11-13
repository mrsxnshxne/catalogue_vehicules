from fastapi import APIRouter

from catalogue_vehicules.schemas.vehicule import VehicleSchema
from catalogue_vehicules.services.engine.diesel_engine_service import DieselEngineService
from catalogue_vehicules.services.engine.electric_engine_service import ElectricEngineService
from catalogue_vehicules.services.engine.gasoline_engine_service import GasolineEngineService
from catalogue_vehicules.services.engine.hybrid_engine_service import HybridEngineService
from catalogue_vehicules.services.vehicle.car_service import CarService
from catalogue_vehicules.services.vehicle.moto_service import MotoService
from catalogue_vehicules.services.vehicle.trunk_service import TruckService


engineRouter = APIRouter(prefix="/engine", tags=["engine"])


@engineRouter.get("/")
async def list_all_engines():
    electric_service = ElectricEngineService()
    diesel_service = DieselEngineService()
    gasoline_service = GasolineEngineService()
    hybrid_service = HybridEngineService()

    electric_engines = electric_service.get()
    diesel_engines = diesel_service.get()
    gasoline_engines = gasoline_service.get()
    hybrid_engines = hybrid_service.get()

    return {
        "electric": electric_engines,
        "diesel": diesel_engines,
        "gasoline": gasoline_engines,
        "hybrid": hybrid_engines,
    }


@engineRouter.get("/{type}")
async def list_engines(type: str):
    if type == "electric":
        service = ElectricEngineService()
        engines = service.get()
        return engines
    elif type == "diesel":
        service = DieselEngineService()
        engines = service.get()
        return engines
    elif type == "gasoline":
        service = GasolineEngineService()
        engines = service.get()
        return engines
    elif type == "hybrid":
        service = HybridEngineService()
        engines = service.get()
        return engines
    else:
        return {"error": "Invalid engine type"}


@engineRouter.get("/{type}/{id}")
async def get_engine(type: str, id: int):
    if type == "electric":
        service = ElectricEngineService()
        engine = service.find(id)
        return engine
    elif type == "diesel":
        service = DieselEngineService()
        engine = service.find(id)
        return engine
    elif type == "gasoline":
        service = GasolineEngineService()
        engine = service.find(id)
        return engine
    elif type == "hybrid":
        service = HybridEngineService()
        engine = service.find(id)
        return engine
    else:
        return {"error": "Invalid engine type"}


@engineRouter.post("/")
async def create_engine(vehicle: VehicleSchema):
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


@engineRouter.delete("/{id}")
async def delete_engine(id: int):
    service = CarService()
    service.delete(id)
    return { "message": "Car deleted successfully" }