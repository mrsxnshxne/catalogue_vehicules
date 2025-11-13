"""
Car data validator module.
"""

from functools import wraps

VALID_MOTOR_TYPES = {"gasoline", "diesel", "hybrid", "electric"}


def validate_car_data(func):
    """
    Decorator to validate car data before processing.
    :param func: The function to be decorated.
    :return: The wrapped function.
    :rtype: function
    :raises ValueError: If validation fails.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        data = args[1]
        required_fields = [
            ("brand", str),
            ("model", str),
            ("year", int),
            ("kilometers", int),
            ("engine_type", str),
            ("trunk", int),
        ]

        for field, field_type in required_fields:
            if field not in data:
                raise ValueError(f"Le champ '{field}' est obligatoire.")
            if not isinstance(data[field], field_type):
                raise ValueError(f"Le champ '{field}' doit être de type {field_type}.")

        if data["engine_type"] not in VALID_MOTOR_TYPES:
            raise ValueError(
                f"Type de moteur invalide. Autorisés : {', '.join(VALID_MOTOR_TYPES)}"
            )

        if (data["engine_type"] == "diesel") or (data["engine_type"] == "gasoline"):
            thermic_required_fields = [
                ("engine_tank_capacity", int),
                ("engine_tank_consumption", (int, float)),
                ("engine_power_gasoline", int),
            ]
            for field, field_type in thermic_required_fields:
                if field not in data:
                    raise ValueError(
                        f"Le champ '{field}' est obligatoire pour un véhicule thermique."
                    )
                if not isinstance(data[field], field_type):
                    raise ValueError(
                        f"Le champ '{field}' doit être de type {field_type}."
                    )

        if data["engine_type"] == "electric":
            electric_required_fields = [
                ("engine_battery_capacity", int),
                ("engine_battery_consumption", (int, float)),
                ("engine_power_electric", int),
            ]
            for field, field_type in electric_required_fields:
                if field not in data:
                    raise ValueError(
                        f"Le champ '{field}' est obligatoire pour un véhicule electrique."
                    )
                if not isinstance(data[field], field_type):
                    raise ValueError(
                        f"Le champ '{field}' doit être de type {field_type}."
                    )

        if data["engine_type"] == "hybrid":
            hybrid_required_fields = [
                ("engine_battery_consumption", (int, float)),
                ("engine_tank_consumption", (int, float)),
                ("engine_power_gasoline", int),
                ("engine_power_electric", int),
                ("engine_battery_capacity", int),
                ("engine_tank_capacity", int),
            ]
            for field, field_type in hybrid_required_fields:
                if field not in data:
                    raise ValueError(
                        f"Le champ '{field}' est obligatoire pour un véhicule hybride."
                    )
                if not isinstance(data[field], field_type):
                    raise ValueError(
                        f"Le champ '{field}' doit être de type {field_type}."
                    )

        return func(*args, **kwargs)

    return wrapper
