import unittest
from battery_manager import BatteryManager

class TestBatteryManager(unittest.TestCase):

    def setUp(self):
        self.battery_manager = BatteryManager()

    # Test Initial Battery Level
    def test_initial_battery_level(self):
        self.assertEqual(self.battery_manager.get_battery_level(), 100)

    # Test Drain Battery
    def test_drain_battery(self):
        self.battery_manager.drain('patrol')
        self.assertEqual(self.battery_manager.get_battery_level(), 100 - BatteryManager.PATROL_DRAIN_RATE)

        self.battery_manager.drain('detection')
        expected_level = 100 - BatteryManager.PATROL_DRAIN_RATE - BatteryManager.DETECTION_DRAIN_RATE
        self.assertEqual(self.battery_manager.get_battery_level(), expected_level)

        self.battery_manager.drain('idle')
        expected_level -= BatteryManager.IDLE_DRAIN_RATE
        self.assertEqual(self.battery_manager.get_battery_level(), expected_level)

    # Test Battery Does Not Go Below 0
    def test_battery_not_below_zero(self):
        for _ in range(200):
            self.battery_manager.drain('patrol')
        self.assertGreaterEqual(self.battery_manager.get_battery_level(), 0)

    # Test Charging Battery
    def test_charge_battery(self):
        self.battery_manager.drain('patrol')
        self.battery_manager.charge(10)
        expected_level = min(100, 100 - BatteryManager.PATROL_DRAIN_RATE + 10)
        self.assertEqual(self.battery_manager.get_battery_level(), expected_level)

    # Test Battery Level Does Not Exceed 100
    def test_battery_not_exceed_100(self):
        self.battery_manager.charge(10)
        self.assertLessEqual(self.battery_manager.get_battery_level(), 100)

    # Test Needs Charging
    def test_needs_charging(self):
        self.battery_manager.battery_level = 21
        self.assertFalse(self.battery_manager.needs_charging())
        self.battery_manager.battery_level = 20
        self.assertTrue(self.battery_manager.needs_charging())