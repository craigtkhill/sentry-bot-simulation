from config import Config
from battery_manager import BatteryManager
from facial_recognition import FacialRecognition
from alarm import Alarm
from notification import Notification
from sensor_processor import SensorProcessor
from security_bot import SecurityBot

if __name__ == "__main__":
    config = Config()
    battery_manager = BatteryManager()
    sensor_processor = SensorProcessor()
    facial_recognition = FacialRecognition()
    alarm = Alarm()
    notification = Notification(config.user_contact, config.security_company_contact, alarm)

    bot = SecurityBot(config, battery_manager, sensor_processor, facial_recognition, alarm, notification)
    bot.turn_on()