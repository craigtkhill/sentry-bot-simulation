import unittest
from unittest.mock import Mock, patch
from bot_behaviour import BotBehaviour

class TestBotBehaviour(unittest.TestCase):

    def setUp(self):
        self.mock_bot = Mock()
        self.bot_behaviour = BotBehaviour(self.mock_bot)

    def test_patrol_initializes_properly(self):
        with patch.object(self.bot_behaviour, 'perform_patrol_iteration') as mock_perform:
            mock_perform.side_effect = [None, Exception("Exit loop")]
            with self.assertRaises(Exception):
                self.bot_behaviour.patrol()
            self.mock_bot.configuration.check_config.assert_called_once()
            self.assertEqual(self.mock_bot.status, 'patrolling')

    def test_perform_patrol_iteration_calls_correct_method(self):
        self.mock_bot.status = 'patrolling'
        with patch('time.sleep'), patch('builtins.print'), patch.object(self.bot_behaviour, '_handle_patrolling') as mock_handle:
            self.bot_behaviour.perform_patrol_iteration()
            mock_handle.assert_called_once()

    def test_handle_patrolling(self):
        self.mock_bot.status = 'patrolling'
        self.mock_bot.configuration.max_area = 10
        self.mock_bot.configuration.get_speed.return_value = 5
        self.mock_bot.battery_manager.needs_charging.return_value = False
        self.mock_bot.alarm.waiting_for_security = False

        with patch.object(self.bot_behaviour, 'handle_detection'):
            self.bot_behaviour._handle_patrolling()
            self.mock_bot.battery_manager.drain.assert_called_with('patrol')
            self.mock_bot.configuration.update_location.assert_called_with(5)

    def test_handle_return_to_station(self):
        self.mock_bot.status = 'return to station'
        self.mock_bot.configuration.get_speed.return_value = 5
        self.mock_bot.battery_manager.get_battery_level.return_value = 4

        self.bot_behaviour._handle_return_to_station()
        self.mock_bot.battery_manager.drain.assert_called_with('idle')
        self.assertEqual(self.mock_bot.status, 'charging')

    def test_handle_charging(self):
        self.mock_bot.status = 'charging'
        self.mock_bot.configuration.get_speed.return_value = 5
        self.mock_bot.battery_manager.get_battery_level.return_value = 100

        self.bot_behaviour._handle_charging()
        self.mock_bot.battery_manager.charge.assert_called_with(5)
        self.assertEqual(self.mock_bot.status, 'patrolling')

    def test_handle_detection(self):
        with patch('random.random', return_value=0.04), patch.object(self.bot_behaviour, 'process_identified_face') as mock_process:
            self.bot_behaviour.handle_detection()
            mock_process.assert_called()

    def test_process_identified_face_with_known_face(self):
        known_face = "John Doe"
        self.mock_bot.facial_recognition.identify_face.return_value = known_face
        self.mock_bot.facial_recognition.is_known_face.return_value = True

        self.bot_behaviour.process_identified_face(known_face)
        self.assertEqual(self.mock_bot.detection_state, "Known individual detected.")

    def test_process_identified_face_with_unknown_face(self):
        unknown_face = "Unknown"
        self.mock_bot.facial_recognition.identify_face.return_value = unknown_face
        self.mock_bot.facial_recognition.is_known_face.return_value = False

        with patch.object(self.bot_behaviour, 'handle_unrecognized_face') as mock_handle:
            self.bot_behaviour.process_identified_face(unknown_face)
            mock_handle.assert_called_with(unknown_face)
            self.assertEqual(self.mock_bot.detection_state, "Unrecognized face detected!")

    def test_handle_unrecognized_face_triggers_alarm(self):
        self.mock_bot.notification.send_user_notification.return_value = 'no'
        self.bot_behaviour.handle_unrecognized_face('unknown_face')
        self.mock_bot.alarm.trigger_alarm.assert_called_once()
        self.mock_bot.notification.alert_security_company.assert_called_with('unknown_face')

    def test_handle_unrecognized_face_does_not_trigger_alarm(self):
        self.mock_bot.notification.send_user_notification.return_value = 'yes'
        self.bot_behaviour.handle_unrecognized_face('unknown_face')
        self.mock_bot.alarm.trigger_alarm.assert_not_called()
        self.mock_bot.notification.alert_security_company.assert_not_called()

    
