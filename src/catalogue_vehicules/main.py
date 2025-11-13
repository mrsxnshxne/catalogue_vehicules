"""
Main module
"""
import uvicorn
from fastapi import FastAPI

from catalogue_vehicules.routers.engine import engineRouter
from catalogue_vehicules.routers.vehicule import vehicleRouter


def main():
    app = FastAPI()
    app.include_router(vehicleRouter)
    app.include_router(engineRouter)
    uvicorn.run(app, port=8000)


if __name__ == '__main__':
    main()