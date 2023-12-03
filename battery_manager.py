# battery_manager.py

class BatteryManager:
    # Class constants for battery thresholds and drain rates
    LOW_BATTERY_THRESHOLD = 20  # Threshold for low battery
    IDLE_DRAIN_RATE = 0.1       # Battery drain rate when idle
    PATROL_DRAIN_RATE = 0.5     # Battery drain rate during patrol
    DETECTION_DRAIN_RATE = 0.3  # Battery drain rate during detection

    def __init__(self):
        # Initial battery level set to 100%
        self.battery_level = 100

    def drain(self, activity):
        # Drain battery based on the type of activity
        if activity == 'patrol':
            self.battery_level -= self.PATROL_DRAIN_RATE
        elif activity == 'detection':
            self.battery_level -= self.DETECTION_DRAIN_RATE
        elif activity == 'idle':
            self.battery_level -= self.IDLE_DRAIN_RATE

        # Ensure battery level does not go below 1%
        self.battery_level = max(1, self.battery_level)

    def charge(self, amount):
        # Charge the battery by a certain amount
        if amount > 0:
            self.battery_level = min(100, self.battery_level + amount)

    def get_battery_level(self):
        # Return the current battery level
        return self.battery_level

    def needs_charging(self):
        # Check if the battery needs charging (below the low battery threshold)
        return self.battery_level <= self.LOW_BATTERY_THRESHOLD
