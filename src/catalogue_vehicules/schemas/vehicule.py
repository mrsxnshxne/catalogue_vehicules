from pydantic import BaseModel


class VehicleSchema(BaseModel):
    type: str

    # Common fields
    brand: str
    model: str
    year: int
    kilometers: int | None = None

    # Engine specific
    engine_id: str

    # Car specific
    trunk: int | None = None

    # Moto specific
    license: str | None = None

    # Truck specific
    max_weight: int | None = None