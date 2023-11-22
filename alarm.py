class Alarm:
    def __init__(self):
        self.is_active = False
        self.snooze_active = False
        self.silent_mode = False

    def trigger_alarm(self):
        if self.snooze_active:
            print("Alarm is snoozed.")
        elif self.silent_mode:
            print("Silent alarm activated. Notifying authorities.")
        else:
            print("Alarm triggered! Loud alarm is sounding.")
            self.is_active = True

    def set_snooze(self, duration):
        self.snooze_active = True
        print(f"Alarm snoozed for {duration} seconds.")

    def disable_snooze(self):
        self.snooze_active = False
        print("Snooze disabled.")

    def set_silent_mode(self, silent):
        self.silent_mode = silent
        mode = 'enabled' if silent else 'disabled'
        print(f"Silent mode {mode}.")

    def reset_alarm(self):
        self.is_active = False
        self.snooze_active = False
        self.silent_mode = False
        print("Alarm reset to default state.")
