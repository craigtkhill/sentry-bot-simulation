import unittest
from unittest.mock import patch
from alarm import Alarm

class TestAlarm(unittest.TestCase):

    def setUp(self):
        self.alarm = Alarm()

    def test_trigger_alarm_normal(self):
        with patch('builtins.print') as mocked_print:
            self.alarm.trigger_alarm()
            self.assertTrue(self.alarm.is_active)
            self.assertTrue(self.alarm.waiting_for_security)
            self.assertGreater(self.alarm.security_arrival_countdown, 0)
            mocked_print.assert_called_with("Alarm triggered! Loud alarm is sounding.")

    def test_trigger_alarm_snoozed(self):
        with patch('builtins.print') as mocked_print:
            self.alarm.snooze_active = True
            self.alarm.trigger_alarm()
            mocked_print.assert_called_with("Alarm is snoozed.")

    def test_trigger_alarm_silent(self):
        with patch('builtins.print') as mocked_print:
            self.alarm.set_silent_mode(True)
            self.alarm.trigger_alarm()
            mocked_print.assert_called_with("Silent alarm activated. Notifying authorities.")

    def test_reset_alarm(self):
        self.alarm.trigger_alarm()
        self.alarm.reset_alarm()
        self.assertFalse(self.alarm.is_active)
        self.assertFalse(self.alarm.snooze_active)
        self.assertFalse(self.alarm.silent_mode)
        self.assertFalse(self.alarm.waiting_for_security)

    def test_set_silent_mode(self):
        with patch('builtins.print') as mocked_print:
            self.alarm.set_silent_mode(True)
            self.assertTrue(self.alarm.silent_mode)
            mocked_print.assert_called_with("Silent mode enabled.")

            self.alarm.set_silent_mode(False)
            self.assertFalse(self.alarm.silent_mode)
            mocked_print.assert_called_with("Silent mode disabled.")
