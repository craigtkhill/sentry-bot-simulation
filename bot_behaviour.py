import random
import time

class BotBehaviour:
    def __init__(self, bot):
        # Initialize with a reference to the bot object
        self.bot = bot

    def patrol(self):
        # Perform patrol activities
        self.bot.configuration.check_config()  # Check the bot's configuration
        self.bot.status = 'patrolling'         # Set the bot's status to patrolling
        while True:
            self.perform_patrol_iteration()    # Continuously perform patrol iterations

    def perform_patrol_iteration(self):
        # Perform a single iteration of patrol
        time.sleep(0.1)  # Short pause between iterations
        print(self.bot, end='\r')  # Print the bot's current state, overwriting the same line
        # Dynamically call the method based on the bot's status
        getattr(self, f"_handle_{self.bot.status.replace(' ', '_')}")()

    def _handle_patrolling(self):
        # Handle the bot's behavior when it is patrolling
        self.bot.battery_manager.drain('patrol')  # Drain battery for patrol activity
        # Update the bot's location if it has a maximum area to patrol
        if self.bot.configuration.max_area > 0:
            self.bot.configuration.update_location(self.bot.configuration.get_speed())
        # Check if the bot needs to go to the charging station
        if self.bot.battery_manager.needs_charging():
            self.bot.go_to_charging_station()
        # Handle security arrival countdown if waiting for security
        if self.bot.alarm.waiting_for_security:
            self.bot.alarm.update_security_arrival_countdown()
        else:
            self.handle_detection()  # Handle detection of faces or objects

    def _handle_return_to_station(self):
        # Handle the bot's behavior when returning to the charging station
        self.bot.battery_manager.drain('idle')  # Drain battery at idle rate while returning
        # Change status to charging if the battery level is low enough
        if self.bot.battery_manager.get_battery_level() <= self.bot.configuration.get_speed():
            self.bot.status = 'charging'

    def _handle_charging(self):
        # Handle the bot's behavior when it is charging
        self.bot.battery_manager.charge(self.bot.configuration.get_speed())  # Charge the battery
        # Switch back to patrolling when fully charged
        if self.bot.battery_manager.get_battery_level() >= 100:
            self.bot.status = 'patrolling'

    def handle_detection(self):
        # Handle detection of faces or objects
        if random.random() < 0.05:  # Random chance to detect a face
            face_identified = self.bot.facial_recognition.identify_face()
            self.process_identified_face(face_identified)

    def process_identified_face(self, face_identified):
        # Process the identified face
        if not face_identified:
            self.bot.detection_state = "No one encountered."
            return

        # Determine if the face is known or unknown
        self.bot.detection_state = "Known individual detected." if self.bot.facial_recognition.is_known_face(face_identified) else "Unrecognized face detected!"
        print(f"{self.bot.detection_state}: {face_identified}")

        # Handle an unrecognized face
        if not self.bot.facial_recognition.is_known_face(face_identified):
            self.handle_unrecognized_face(face_identified)

    def handle_unrecognized_face(self, face_identified):
        # Handle an unrecognized face
        self.bot.display_random_image()  # Display a random image
        user_recognition = self.bot.notification.send_user_notification(face_identified)
        # Trigger alarm if the user does not recognize the face
        if user_recognition != 'yes':
            print("Unrecognized face by user. Sounding the alarm!")
            self.bot.alarm.trigger_alarm()
            self.bot.notification.alert_security_company(face_identified)
        else:
            print("Face recognized by user. No alarm.")
            # Add the recognized face to the known faces
            self.bot.facial_recognition.add_face(face_identified)
