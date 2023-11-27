import unittest
from unittest.mock import patch
from notification import Notification  # Modify this import based on your project structure

class TestNotification(unittest.TestCase):

    def setUp(self):
        user_contact = "user@example.com"
        security_company_contact = "security@example.com"
        self.notification = Notification(user_contact, security_company_contact)

    @patch('builtins.input', side_effect=['yes'])
    def test_send_user_notification_yes(self, mock_input):
        response = self.notification.send_user_notification("face123")
        self.assertEqual(response, 'yes')
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['no'])
    def test_send_user_notification_no(self, mock_input):
        response = self.notification.send_user_notification("face123")
        self.assertEqual(response, 'no')
        self.assertTrue(mock_input.called)

    @patch('builtins.print')
    def test_alert_security_company(self, mock_print):
        self.notification.alert_security_company("face123")
        mock_print.assert_called_with("Alert sent to security company: Unrecognized face detected! face123")
