class Alarm:
    def __init__(self):
        self.status = 'off'
        self.snooze_active = False
        self.silent_mode = False

    def trigger_alarm(self):
        """ Triggers the alarm based on the current settings. """
        if self.snooze_active:
            print("Alarm is snoozed.")
        elif self.silent_mode:
            print("Silent alarm activated. Notifying authorities.")
            # Add logic to notify authorities or homeowners silently.
        else:
            print("Alarm triggered! Loud alarm is sounding.")
            # Add logic to activate the physical alarm system.

    def set_snooze(self, duration):
        """ Sets the alarm to snooze for a given duration. """
        self.snooze_active = True
        # Add logic to handle the duration of snooze if necessary.
        print(f"Alarm snoozed for {duration} seconds.")

    def disable_snooze(self):
        """ Disables the snooze feature. """
        self.snooze_active = False
        print("Snooze disabled.")

    def set_silent_mode(self, silent):
        """ Enables or disables the silent mode. """
        self.silent_mode = silent
        mode = 'enabled' if silent else 'disabled'
        print(f"Silent mode {mode}.")

    def reset_alarm(self):
        """ Resets the alarm to its default state. """
        self.status = 'off'
        self.snooze_active = False
        self.silent_mode = False
        print("Alarm reset to default state.")
