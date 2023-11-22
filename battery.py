class BatteryManager:
    LOW_BATTERY_THRESHOLD = 20

    def __init__(self):
        self.bat_level = 100
    
    def drain(self, amount):
        self.bat_level = max(0, self.bat_level - amount)

    def charge(self, amount):
        self.bat_level = min(100, self.bat_level + amount)

    def get_battery_level(self):
        return self.bat_level

    def needs_charging(self):
        return self.bat_level < self.LOW_BATTERY_THRESHOLD
