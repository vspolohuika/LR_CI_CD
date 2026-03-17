class TooMuchFuelError(Exception):
    """Исключение при попытке залить слишком много топлива."""

class NotEnoughFuelError(Exception):
    """Исключение при недостатке топлива для поездки."""

class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        too_much_fuel_msg = "Вы пытаетесь залить слишком много бензина!"
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise TooMuchFuelError(too_much_fuel_msg)
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        # Считаем, что расход 8 литров на 100 км
        fuel_burned: float = 8 * (distance_km / 100)
        not_enought_fuel_msg = "Не доедем жеж..."
        if self._fuel_in_tank < fuel_burned:
            raise NotEnoughFuelError(not_enought_fuel_msg)
        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
