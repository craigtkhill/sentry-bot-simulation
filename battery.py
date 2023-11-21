class BatteryManager:

    def __init__(self):
        self.bat_level = 100
    
    def drain(self, speed: int):
        self.bat_level -= speed

    def get_battery_level(self):
        return self.bat_level

    def needs_charging(self):
        if self.get_battery_level() < 20:
            return True

    def charge(self, speed: int):
        self.bat_level += speed
