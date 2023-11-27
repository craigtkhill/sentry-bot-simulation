#battery_manager.py

class BatteryManager:
    LOW_BATTERY_THRESHOLD = 20
    IDLE_DRAIN_RATE = 0.1
    PATROL_DRAIN_RATE = 0.5
    DETECTION_DRAIN_RATE = 0.3
    # You can add other specific activities and their respective drain rates

    def __init__(self):
        self.battery_level = 100

    def drain(self, activity):
        if activity == 'patrol':
            self.battery_level -= self.PATROL_DRAIN_RATE
        elif activity == 'detection':
            self.battery_level -= self.DETECTION_DRAIN_RATE
        elif activity == 'idle':
            self.battery_level -= self.IDLE_DRAIN_RATE
        # Implement other conditions for different activities

        # Ensure the battery level doesn't go below 0
        self.battery_level = max(0, self.battery_level)

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)

    def get_battery_level(self):
        return self.battery_level

    def needs_charging(self):
        return self.battery_level <= self.LOW_BATTERY_THRESHOLD
