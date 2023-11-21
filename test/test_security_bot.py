import unittest
from unittest.mock import patch, MagicMock
from security_bot import SecurityBot
from config import Config
from battery import BatteryManager
from sensor import SensorProcessor

class TestSecurityBot(unittest.TestCase):

    def setUp(self):
        self.bot = SecurityBot()

    def test_get_battery_icon(self):
        # Test for different statuses
        self.bot.status = 'patrolling'
        self.assertEqual(self.bot.get_battery_icon(), '🔋')
        self.bot.status = 'return to station'
        self.assertEqual(self.bot.get_battery_icon(), '🔌')
        self.bot.status = 'charging'
        self.assertEqual(self.bot.get_battery_icon(), '⚡')

    def test_perform_patrol_iteration_behavior(self):
        with patch('time.sleep'), patch.object(self.bot, '_handle_patrolling'):
            self.bot.status = 'patrolling'
            self.bot._perform_patrol_iteration()
            self.bot._handle_patrolling.assert_called_once()

    def test_handle_return_to_station(self):
        self.bot.status = 'return to station'
        self.bot.battery_manager.get_battery_level = MagicMock(return_value=1)
        self.bot.battery_manager.charge = MagicMock()
        self.bot._handle_return_to_station()
        self.assertEqual(self.bot.status, 'charging')
        self.bot.battery_manager.charge.assert_called_once()

    def test_handle_charging(self):
        self.bot.status = 'charging'
        self.bot.battery_manager.get_battery_level = MagicMock(return_value=100)
        self.bot.battery_manager.charge = MagicMock()
        self.bot._handle_charging()
        self.assertEqual(self.bot.status, 'patrolling')
        self.bot.battery_manager.charge.assert_called_once()

    
        



