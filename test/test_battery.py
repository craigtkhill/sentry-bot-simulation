import unittest
from battery import BatteryManager

class TestBatteryManager(unittest.TestCase):
    def setUp(self):
        self.battery = BatteryManager()

    def test_get_battery_level(self):
        self.assertEqual(self.battery.get_battery_level(), 100)

    def test_needs_charging(self):
        self.assertFalse(self.battery.needs_charging())
        self.battery.bat_level = 19
        self.assertTrue(self.battery.needs_charging())

    def test_drain(self):
        self.battery.drain(1)
        self.assertEqual(self.battery.get_battery_level(), 99)

    def test_charge(self):
        self.battery.bat_level = 19
        self.battery.charge(10)
        self.assertEqual(self.battery.get_battery_level(), 29)

        





    