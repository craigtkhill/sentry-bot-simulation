import time
import random
import os
from PIL import Image


class SecurityBot:
    def __init__(self, config, battery_manager, sensor_processor, facial_recognition, alarm, notification):
        self.configuration = config
        self.battery_manager = battery_manager
        self.sensor_processor = sensor_processor
        self.facial_recognition = facial_recognition
        self.alarm = alarm
        self.notification = notification
        self.status = 'off'
        self.detection_state = 'No detection yet'

    def __str__(self):
        battery_icon = self.get_battery_icon()
        return (f'SecurityBot: {self.status.title()} {battery_icon}:'
                f'{self.battery_manager.get_battery_level()}% '
                f'Covered:{self.configuration.current_location}/'
                f'{self.configuration.max_area}m | Detection: {self.detection_state}')

    def get_battery_icon(self):
        icons = {'patrolling': '🔋', 'return to station': '🔌', 'charging': '⚡'}
        return icons.get(self.status, '')

    def patrol(self):
        self.configuration.check_config()
        self.status = 'patrolling'
        while True:
            self._perform_patrol_iteration()

    def _perform_patrol_iteration(self):
        time.sleep(0.1)
        print(self, end='\r')
        getattr(self, f"_handle_{self.status.replace(' ', '_')}")()

    def _handle_patrolling(self):
        self.battery_manager.drain(self.configuration.get_speed())
        if self.configuration.max_area > 0:
            self.configuration.update_location(self.configuration.get_speed())
        if self.battery_manager.needs_charging():
            self.go_to_charging_station()
        else:
            self.handle_detection()

    def _handle_return_to_station(self):
        self.battery_manager.drain(self.configuration.get_speed())
        if self.battery_manager.get_battery_level() <= self.configuration.get_speed():
            self.status = 'charging'

    def _handle_charging(self):
        self.battery_manager.charge(self.configuration.get_speed())
        if self.battery_manager.get_battery_level() >= 100:
            self.status = 'patrolling'

    def handle_detection(self):
        if random.random() < 0.05:
            face_identified = self.facial_recognition.identify_face()
            self.process_identified_face(face_identified)

    def process_identified_face(self, face_identified):
        if not face_identified:
            self.detection_state = "No one encountered."
            return

        self.detection_state = "Known individual detected." if self.facial_recognition.is_known_face(face_identified) else "Unrecognized face detected!"
        print(f"{self.detection_state}: {face_identified}")

        if not self.facial_recognition.is_known_face(face_identified):
            self.handle_unrecognized_face(face_identified)

    def handle_unrecognized_face(self, face_identified):
        user_recognition = input("Do you recognize this face? (yes/no): ").strip().lower()
        if user_recognition != 'yes':
            print("Unrecognized face by user. Sounding the alarm!")
            self.alarm.trigger_alarm()
        else:
            print("Face recognized by user. No alarm.")
            self.facial_recognition.add_face(face_identified)

    def go_to_charging_station(self):
        self.status = 'return to station'

    def turn_on(self):
        print('Turning on Security Bot...')
        self.patrol()

    def display_random_image(self):
        faces_folder = 'faces/'
        image_files = [f for f in os.listdir(faces_folder) if f.endswith('.png')]
        if image_files:
            img = Image.open(os.path.join(faces_folder, random.choice(image_files)))
            img.show()
        else:
            print("No images found in the folder.")
