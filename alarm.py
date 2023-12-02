import random
import time

class Alarm:
    def __init__(self):
        # Initial state of the alarm
        self.is_active = False
        self.snooze_active = False
        self.silent_mode = False
        self.waiting_for_security = False
        self.security_arrival_countdown = 0

    def trigger_alarm(self):
        # Check if the alarm is snoozed
        if self.snooze_active:
            print("Alarm is snoozed.")
        # Check if the alarm is in silent mode
        elif self.silent_mode:
            print("Silent alarm activated. Notifying authorities.")
        else:
            # Activate the alarm in loud mode
            print("Alarm triggered! Loud alarm is sounding.")
            self.is_active = True
            self.waiting_for_security = True
            # Random time for security to arrive
            self.security_arrival_countdown = random.randint(5, 15) 

    def security_check_done(self):
        # Security check is complete
        print("Security company has checked. Resetting alarm.")
        self.reset_alarm()

    def set_silent_mode(self, silent):
        # Set or unset the silent mode
        self.silent_mode = silent
        mode = 'enabled' if silent else 'disabled'
        print(f"Silent mode {mode}.")

    def reset_alarm(self):
        # Reset the alarm to its default state
        self.is_active = False
        self.snooze_active = False
        self.silent_mode = False
        self.waiting_for_security = False
        print("Alarm reset to default state.")

    def update_security_arrival_countdown(self):
        # Update the countdown for security arrival
        if self.waiting_for_security and self.security_arrival_countdown > 0:
            print(f"Security arriving in {self.security_arrival_countdown} ", end='\r')
            self.security_arrival_countdown -= 1
            time.sleep(1)
            # When countdown reaches zero, perform security check
            if self.security_arrival_countdown <= 0:
                self.security_check_done()
