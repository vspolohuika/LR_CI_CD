# Собственные классы исключений.


class TooMuchFuelError(Exception):
    """Исключение при попытке залить слишком много бензина."""


class NotEnoughFuelError(Exception):
    """Исключение при недостатке бензина для поездки."""


# Константы для сообщений об ошибках.
TOO_MUCH_FUEL_MSG = "Вы пытаетесь залить слишком много бензина!"
NOT_ENOUGH_FUEL_MSG = "Не доедем жеж..."


class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self.model = model
        self._fuel_in_tank: float = 0.0
        self._max_fuel_capacity: float = fuel_capacity

    def refuel_car(self, fuel_quantity: float) -> None:
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise TooMuchFuelError(TOO_MUCH_FUEL_MSG)
        self._fuel_in_tank += fuel_quantity

    def drive_car(self, distance_km: float) -> float:
        # Считаем, что расход 8 литров на 100 км.
        fuel_burned: int = 8 * (distance_km / 100)
        if self._fuel_in_tank < fuel_burned:
            raise NotEnoughFuelError(NOT_ENOUGH_FUEL_MSG)
        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank
