import unittest
from .car import Car, TooMuchFuelError, NotEnoughFuelError

class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def tearDown(self):
        pass

    def test_drive(self):
        # Сначала нужно заправить машину
        self.car.refuel_car(20)
        # Проехать 20 км (сгорит 1.6 литра)
        self.car.drive_car(20)
        # Проверить, что нельзя проехать 80000 км без топлива
        self.assertRaises(NotEnoughFuelError, lambda: self.car.drive_car(80000))

    def test_refuel(self):
        # Заправим 20 литров
        self.car.refuel_car(20)
        assert self.car.get_current_fuel_level() == 20
        # Проверим, что будет исключение, если перельем
        self.assertRaises(TooMuchFuelError, lambda: self.car.refuel_car(80))
