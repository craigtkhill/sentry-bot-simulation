import time
import sensor
import facial_recognition
import alarm
import notification
import battery
import config

class SecurityBot:
    def __init__(self):
        self.configuration = config.Config()
        self.battery_manager = battery.BatteryManager()
        self.sensor_processor = sensor.SensorProcessor()
        #self.alarms = alarm.Alarm()
        #self.notification = notification.Notification()
        self.status = 'off'

    def get_battery_icon(self):
        if self.status == 'patrolling':
            battery_icon = '🔋'
        elif self.status == 'return to station':
            battery_icon = '🔌'
        elif self.status == 'charging':
            battery_icon = '⚡'
        return battery_icon
    
    def __str__(self) -> str:
        battery_icon = self.get_battery_icon()
        return f'SecurityBot: {self.status.title()} {battery_icon}:{self.battery_manager.get_battery_level()} Covered:{self.configuration.get_current_location}/{self.configuration.get_max_area}m'

    def patrol(self):
        self.configuration.check_config()
        self.status = 'patrolling'
        while True:
            self._perform_patrol_iteration()

    def _perform_patrol_iteration(self):
        time.sleep(0.1)
        print(self)
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
        face_identified = facial_recognition.identify_face()
        if face_identified:
            if not facial_recognition.is_known_face(face_identified):
                alarm.trigger_alarm()
                notification.send_alert(face_identified)
    
    def go_to_charging_station(self):
        self.status = 'return to station'
        self.configuration.return_to_station(self.configuration.get_speed())
    
    def turn_on(self):
        print('Turning on Security Bot...')
        self.patrol()

    def handle_detection(self):
        face_identified = facial_recognition.identify_face()
        if face_identified:
            if not facial_recognition.is_known_face(face_identified):
                alarm.trigger_alarm()
                notification.send_alert(face_identified)

