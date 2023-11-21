import time
import config
import battery
import facial_recognition
import alarm
import notification
import sensor
import random

class SecurityBot:
    def __init__(self):
        self.configuration = config.Config()
        self.battery_manager = battery.BatteryManager()
        self.sensor_processor = sensor.SensorProcessor()
        self.facial_recognition = facial_recognition.FacialRecognition()
        self.alarm = alarm.Alarm()
        self.notification = notification.Notification()
        self.status = 'off'
        self.detection_state = 'No detection yet'  # New attribute for detection state

    def get_battery_icon(self):
        if self.status == 'patrolling':
            return '🔋'
        elif self.status == 'return to station':
            return '🔌'
        elif self.status == 'charging':
            return '⚡'
        else:
            return ''

    def __str__(self) -> str:
        battery_icon = self.get_battery_icon()
        return f'\rSecurityBot: {self.status.title()} {battery_icon}:{self.battery_manager.get_battery_level()}% Covered:{self.configuration.current_location}/{self.configuration.max_area}m | Detection: {self.detection_state}'

    def patrol(self):
        self.configuration.check_config()
        self.status = 'patrolling'
        while True:
            self._perform_patrol_iteration()

    def _perform_patrol_iteration(self):
        time.sleep(0.1)
        print(self, end=' ' * 20)
        
        if self.status == 'patrolling':
            self._handle_patrolling()
        elif self.status == 'return to station':
            self._handle_return_to_station()
        elif self.status == 'charging':
            self._handle_charging()

    def _handle_patrolling(self):
        self.battery_manager.drain(self.configuration.get_speed())
        self.configuration.patrol_location(self.configuration.get_speed())
        if self.battery_manager.needs_charging():
            self.go_to_charging_station()
        else:
            self.handle_detection()

    def _handle_return_to_station(self):
        self.battery_manager.drain(self.configuration.get_speed())
        if self.battery_manager.get_battery_level() <= self.configuration.get_speed():
            self.battery_manager.charge(self.configuration.get_speed())
            self.status = 'charging'
    
    def _handle_charging(self):
        self.battery_manager.charge(self.configuration.get_speed())
        if self.battery_manager.get_battery_level() >= 100:
            self.status = 'patrolling'

    def handle_detection(self):
        # Random chance of encountering a person (e.g., 10%)
        if random.random() < 0.1:
            face_identified = self.facial_recognition.identify_face()
            
            if face_identified:
                self.detection_state = "Intruder detected!"
                self.alarm.trigger_alarm()
                self.notification.send_alert(face_identified)
            else:
                self.detection_state = "Known individual or no threat detected."
        else:
            self.detection_state = "No one encountered."

    def go_to_charging_station(self):
        self.status = 'return to station'
        self.configuration.return_to_station()
    
    def turn_on(self):
        print('Turning on Security Bot...')
        self.patrol()
