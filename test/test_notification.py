import unittest
from unittest.mock import Mock, patch
from notification import Notification

class TestNotification(unittest.TestCase):

    def setUp(self):
        self.mock_alarm = Mock()
        self.notification = Notification("user@example.com", "security@example.com", self.mock_alarm)

    def test_send_user_notification(self):
        face_identified = "John Doe"
        with patch('builtins.input', return_value='yes'):
            response = self.notification.send_user_notification(face_identified)
            self.assertEqual(response, 'yes')

    def test_alert_security_company(self):
        face_identified = "Unknown Person"
        with patch('builtins.print') as mock_print:
            self.notification.alert_security_company(face_identified)
            mock_print.assert_called_with(f"Alert sent to security company: Unrecognized face detected! {face_identified}")
            self.mock_alarm.trigger_alarm.assert_called_once()

    def test_handle_security_response_when_waiting(self):
        self.mock_alarm.waiting_for_security = True
        with patch('random.choice', return_value='yes'):
            self.notification.handle_security_response()
            self.mock_alarm.security_check_done.assert_called_once()

    def test_handle_security_response_when_not_waiting(self):
        self.mock_alarm.waiting_for_security = False
        with patch('random.choice') as mock_random_choice:
            self.notification.handle_security_response()
            mock_random_choice.assert_not_called()
            self.mock_alarm.security_check_done.assert_not_called()
