import unittest
from unittest.mock import patch, mock_open
from config import Config
import json

class TestConfig(unittest.TestCase):

    # Mocking the contents of config.json
    mock_config_data = {
        "MAX_AREA": 5000,
        "DEFAULT_AREA": 1000,
        "DEFAULT_SPEED": 1,
        "MAX_SPEED": 10
    }

    # Test Initialization and Load Config
    def test_initialization_and_load_config(self):
        with patch('builtins.open', mock_open(read_data=json.dumps(self.mock_config_data))):
            config = Config()
            self.assertEqual(config.MAX_AREA, 5000)
            self.assertEqual(config.DEFAULT_AREA, 1000)
            self.assertEqual(config.DEFAULT_SPEED, 1)
            self.assertEqual(config.MAX_SPEED, 10)

    # Test Set Area
    def test_set_area(self):
        config = Config()
        config.set_area(3000)
        self.assertEqual(config.max_area, 3000)
        config.set_area(6000)  # Out of range
        self.assertEqual(config.max_area, config.DEFAULT_AREA)

    # Test Get Speed
    def test_get_speed(self):
        config = Config()
        self.assertEqual(config.get_speed(), config.DEFAULT_SPEED)

    # Test Update Location
    def test_update_location(self):
        config = Config()
        config.set_area(500)  # Set a known area
        config.update_location(250)
        self.assertEqual(config.current_location, 250)
        config.update_location(300)  # This should wrap around
        self.assertEqual(config.current_location, 50)

    # Test Input Config
    def test_input_config(self):
        with patch('builtins.input', side_effect=['3000', '5']), \
             patch('builtins.open', mock_open(read_data=json.dumps(self.mock_config_data))):
            config = Config()
            config.input_config()
            self.assertEqual(config.max_area, 3000)
            self.assertEqual(config.get_speed(), 5)