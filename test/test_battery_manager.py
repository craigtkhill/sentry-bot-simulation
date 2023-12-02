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
