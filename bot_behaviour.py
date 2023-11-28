import random
import time

class BotBehaviour:
    def __init__(self, bot):
        self.bot = bot

    def patrol(self):
        self.bot.configuration.check_config()
        self.bot.status = 'patrolling'
        while True:
            self.perform_patrol_iteration()

    def perform_patrol_iteration(self):
        time.sleep(0.1)
        print(self.bot, end='\r')
        getattr(self, f"_handle_{self.bot.status.replace(' ', '_')}")()

    def _handle_patrolling(self):
        self.bot.battery_manager.drain('patrol')
        if self.bot.configuration.max_area > 0:
            self.bot.configuration.update_location(self.bot.configuration.get_speed())
        if self.bot.battery_manager.needs_charging():
            self.bot.go_to_charging_station()
        if self.bot.alarm.waiting_for_security:
            self.bot.alarm.update_security_arrival_countdown()
        else:
            self.handle_detection()

    def _handle_return_to_station(self):
        self.bot.battery_manager.drain('idle')  # Drain battery at idle rate while returning to station
        if self.bot.battery_manager.get_battery_level() <= self.bot.configuration.get_speed():
            self.bot.status = 'charging'

    def _handle_charging(self):
        self.bot.battery_manager.charge(self.bot.configuration.get_speed())
        if self.bot.battery_manager.get_battery_level() >= 100:
            self.bot.status = 'patrolling'

    def handle_detection(self):
        if random.random() < 0.05:
            face_identified = self.bot.facial_recognition.identify_face()
            self.process_identified_face(face_identified)

    def process_identified_face(self, face_identified):
        if not face_identified:
            self.bot.detection_state = "No one encountered."
            return

        self.bot.detection_state = "Known individual detected." if self.bot.facial_recognition.is_known_face(face_identified) else "Unrecognized face detected!"
        print(f"{self.bot.detection_state}: {face_identified}")

        if not self.bot.facial_recognition.is_known_face(face_identified):
            self.handle_unrecognized_face(face_identified)

    def handle_unrecognized_face(self, face_identified):
        user_recognition = self.bot.notification.send_user_notification(face_identified)
        if user_recognition != 'yes':
            print("Unrecognized face by user. Sounding the alarm!")
            self.bot.alarm.trigger_alarm()
            self.bot.notification.alert_security_company(face_identified)
        else:
            print("Face recognized by user. No alarm.")
            self.bot.facial_recognition.add_face(face_identified)
