import unittest
from unittest.mock import patch, mock_open
from config import Config
import json

class TestConfig(unittest.TestCase):

    def setUp(self):
        # Mock the open function and json.load to provide a controlled environment for testing
        self.config_data = {
            'MAX_AREA': 5000,
            'DEFAULT_AREA': 1000,
            'DEFAULT_SPEED': 1,
            'MAX_SPEED': 10,
            'USER_CONTACT': 'user@example.com',
            'SECURITY_CONTACT': 'security@example.com'
        }
        self.mock_file = mock_open(read_data=json.dumps(self.config_data))
        self.patcher = patch('builtins.open', self.mock_file)
        self.patcher.start()
        self.config = Config()

    def tearDown(self):
        self.patcher.stop()

    def test_load_config(self):
        # Test if the configuration is loaded correctly
        self.assertEqual(self.config.MAX_AREA, 5000)
        self.assertEqual(self.config.DEFAULT_AREA, 1000)
        self.assertEqual(self.config.DEFAULT_SPEED, 1)
        self.assertEqual(self.config.MAX_SPEED, 10)
        self.assertEqual(self.config.user_contact, 'user@example.com')
        self.assertEqual(self.config.security_company_contact, 'security@example.com')

    def test_set_area_within_range(self):
        # Test setting the patrol area within the allowed range
        self.config.set_area(3000)
        self.assertEqual(self.config.max_area, 3000)

    def test_set_area_out_of_range(self):
        # Test setting the patrol area outside the allowed range
        self.config.set_area(6000)
        self.assertEqual(self.config.max_area, self.config.DEFAULT_AREA)

    def test_get_speed(self):
        # Test getting the patrol speed
        self.assertEqual(self.config.get_speed(), self.config.DEFAULT_SPEED)

    def test_update_location(self):
        # Test updating the current location
        initial_location = self.config.current_location
        move_distance = 100
        self.config.update_location(move_distance)
        expected_location = (initial_location + move_distance) % self.config.max_area
        self.assertEqual(self.config.current_location, expected_location)
