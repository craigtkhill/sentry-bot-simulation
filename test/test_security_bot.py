import unittest
from unittest.mock import Mock, patch
from security_bot import SecurityBot
from facial_recognition import FacialRecognition
from PIL import Image

# Mock dependencies
config_mock = Mock()
battery_manager_mock = Mock()
facial_recognition_mock = FacialRecognition()
alarm_mock = Mock()
notification_mock = Mock()

class TestSecurityBot(unittest.TestCase):

    def setUp(self):
        # Set up mocks
        config_mock.max_area = 5000
        battery_manager_mock.get_battery_level.return_value = 100
        self.security_bot = SecurityBot(
            config_mock,
            battery_manager_mock,
            facial_recognition_mock,
            alarm_mock,
            notification_mock
        )

    # Test Initialization
    def test_initialization(self):
        self.assertEqual(self.security_bot.status, 'off')
        self.assertEqual(self.security_bot.detection_state, 'No detection yet')

    # Test Patrol Logic
    def test_patrol_logic(self):
        # This test might require additional setup to handle infinite loops or time delays
        pass

    # Test Battery Drain and Charging
    def test_battery_drain_and_charging(self):
        # Setup initial battery level
        battery_manager_mock.get_battery_level.return_value = 100
        self.security_bot._handle_patrolling()
        battery_manager_mock.drain.assert_called_with('patrol')

        self.security_bot._handle_charging()
        battery_manager_mock.charge.assert_called_with(config_mock.get_speed.return_value)

    # Test Detection Handling
    def test_detection_handling(self):
        # Mock random.choice to control the output of identify_face
        with patch('random.choice', return_value='face_1'):
            face_identified = facial_recognition_mock.identify_face()
            self.assertEqual(face_identified, 'face_1')

    # Test Alarm and Notification
    def test_alarm_and_notification(self):
        with patch('builtins.input', return_value='no'):
            self.security_bot.handle_unrecognized_face('face_1')
        alarm_mock.trigger_alarm.assert_called_once()
        # Add more assertions for different scenarios

    # Test Display Random Image
    def test_display_random_image(self):
        # Mock os.listdir and Image.open
        with patch('os.listdir', return_value=['image1.png']), \
             patch.object(Image, 'open', return_value=Mock()) as mock_open:
            self.security_bot.display_random_image()
            mock_open.assert_called_once()