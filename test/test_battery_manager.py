import unittest
from unittest.mock import patch
from battery_manager import BatteryManager

class TestBatteryManager(unittest.TestCase):

    def setUp(self):
        self.battery_manager = BatteryManager()

    def test_initial_battery_level(self):
        self.assertEqual(self.battery_manager.get_battery_level(), 100)

    def test_drain_battery_patrol(self):
        self.battery_manager.drain('patrol')
        expected_level = 100 - BatteryManager.PATROL_DRAIN_RATE
        self.assertEqual(self.battery_manager.get_battery_level(), expected_level)

    def test_drain_battery_detection(self):
        self.battery_manager.drain('detection')
        expected_level = 100 - BatteryManager.DETECTION_DRAIN_RATE
        self.assertEqual(self.battery_manager.get_battery_level(), expected_level)

    def test_drain_battery_idle(self):
        self.battery_manager.drain('idle')
        expected_level = 100 - BatteryManager.IDLE_DRAIN_RATE
        self.assertEqual(self.battery_manager.get_battery_level(), expected_level)

    def test_battery_does_not_drain_below_1(self):
        for _ in range(1000):  # Drain the battery with a large number of idle activities
            self.battery_manager.drain('idle')
        self.assertEqual(self.battery_manager.get_battery_level(), 1)

    def test_charge_battery(self):
        for _ in range(20):
            self.battery_manager.drain('patrol')  # Drain the battery a bit
        self.battery_manager.charge(1)       # Charge the battery
        self.assertEqual(self.battery_manager.get_battery_level(), 91)

    def test_battery_does_not_charge_above_100(self):
        self.battery_manager.charge(50)  # Attempt to overcharge the battery
        self.assertEqual(self.battery_manager.get_battery_level(), 100)

    def test_needs_charging(self):
        self.battery_manager.battery_level = BatteryManager.LOW_BATTERY_THRESHOLD
        self.assertTrue(self.battery_manager.needs_charging())

        self.battery_manager.battery_level = BatteryManager.LOW_BATTERY_THRESHOLD + 1
        self.assertFalse(self.battery_manager.needs_charging())
# ECP and BVA for the 'charge' method
    def test_charge_battery_with_negative_amount(self):
        initial_level = self.battery_manager.get_battery_level()
        self.battery_manager.charge(-10)  # Invalid negative charge
        # Expect no change in battery level for negative charge
        self.assertEqual(self.battery_manager.get_battery_level(), initial_level)

    def test_charge_battery_with_small_valid_amount(self):
        self.battery_manager.battery_level = 95
        self.battery_manager.charge(4)  # Valid charge that does not exceed 100
        self.assertEqual(self.battery_manager.get_battery_level(), 99)

    def test_charge_battery_with_exact_amount_to_full(self):
        self.battery_manager.battery_level = 80
        self.battery_manager.charge(20)  # Charge exactly to the full level
        self.assertEqual(self.battery_manager.get_battery_level(), 100)

    def test_charge_battery_with_large_valid_amount(self):
        self.battery_manager.battery_level = 50
        self.battery_manager.charge(100)  # Valid charge but exceeds 100
        self.assertEqual(self.battery_manager.get_battery_level(), 100)