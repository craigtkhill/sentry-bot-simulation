import random
import time

class Alarm:
    def __init__(self):
        self.is_active = False
        self.snooze_active = False
        self.silent_mode = False
        self.waiting_for_security = False
        self.security_arrival_countdown = 0

    def trigger_alarm(self):
        if self.snooze_active:
            print("Alarm is snoozed.")
        elif self.silent_mode:
            print("Silent alarm activated. Notifying authorities.")
        else:
            print("Alarm triggered! Loud alarm is sounding.")
            self.is_active = True
            self.waiting_for_security = True
            self.security_arrival_countdown = random.randint(5, 15)  # Random countdown between 5 to 15 seconds

    def security_check_done(self):
        print("Security company has checked. Resetting alarm.")
        self.reset_alarm()

    def set_silent_mode(self, silent):
        self.silent_mode = silent
        mode = 'enabled' if silent else 'disabled'
        print(f"Silent mode {mode}.")

    def reset_alarm(self):
        self.is_active = False
        self.snooze_active = False
        self.silent_mode = False
        self.waiting_for_security = False
        print("Alarm reset to default state.")

    def update_security_arrival_countdown(self):
        if self.waiting_for_security and self.security_arrival_countdown > 0:
            print(f"Security arriving in {self.security_arrival_countdown} seconds.", end='\r')
            self.security_arrival_countdown -= 1
            time.sleep(1)
            if self.security_arrival_countdown <= 0:
                self.security_check_done()