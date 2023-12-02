import unittest
from unittest.mock import Mock, patch
from security_bot import SecurityBot

class TestSecurityBot(unittest.TestCase):

    def setUp(self):
        self.mock_config = Mock()
        self.mock_battery_manager = Mock()
        self.mock_facial_recognition = Mock()
        self.mock_alarm = Mock()
        self.mock_notification = Mock()
        self.security_bot = SecurityBot(self.mock_config, self.mock_battery_manager, 
                                        self.mock_facial_recognition, self.mock_alarm, 
                                        self.mock_notification)

    def test_go_to_charging_station(self):
        self.security_bot.go_to_charging_station()
        self.assertEqual(self.security_bot.status, 'return to station')

    def test_turn_on(self):
        with patch.object(self.security_bot.behaviour, 'patrol') as mock_patrol:
            self.security_bot.turn_on()
            mock_patrol.assert_called_once()