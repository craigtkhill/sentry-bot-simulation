from config import Config
from battery import BatteryManager
from facial_recognition import FacialRecognition
from alarm import Alarm
from notification import Notification
from sensor import SensorProcessor
from security_bot import SecurityBot

if __name__ == "__main__":
    config = Config()
    battery_manager = BatteryManager()
    sensor_processor = SensorProcessor()
    facial_recognition = FacialRecognition()
    alarm = Alarm()
    notification = Notification()

    bot = SecurityBot(config, battery_manager, sensor_processor, facial_recognition, alarm, notification)
    bot.turn_on()