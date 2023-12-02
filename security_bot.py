#security_bot.py
import os
from PIL import Image
import random
from bot_behaviour import BotBehaviour

class SecurityBot:
    def __init__(self, config, battery_manager, facial_recognition, alarm, notification):
        self.configuration = config
        self.battery_manager = battery_manager
        self.facial_recognition = facial_recognition
        self.alarm = alarm
        self.notification = notification
        self.status = 'off'
        self.detection_state = 'No detection yet'
        self.behaviour = BotBehaviour(self)

    def __str__(self):
        battery_icon = self.get_battery_icon()
        return (f'SecurityBot: {self.status.title()} {battery_icon}:'
                f'{round(self.battery_manager.get_battery_level())}% '
                f'Covered:{self.configuration.current_location}/'
                f'{self.configuration.max_area}m | Detection: {self.detection_state}')

    def get_battery_icon(self):
        icons = {'patrolling': '🔋', 'return to station': '🔌', 'charging': '⚡'}
        return icons.get(self.status, '')

    def go_to_charging_station(self):
        self.status = 'return to station'

    def turn_on(self):
        print('Turning on Security Bot...')
        self.behaviour.patrol()

    def display_random_image(self):
        faces_folder = 'faces/'
        image_files = [f for f in os.listdir(faces_folder) if f.endswith('.png')]
        if image_files:
            img = Image.open(os.path.join(faces_folder, random.choice(image_files)))
            img.show()
        else:
            print("No images found in the folder.")
