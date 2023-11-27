# config.py
import json

class Config:
    def __init__(self):
        self.load_config()

    def load_config(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
            self.MAX_AREA = config.get('MAX_AREA', 5000)  # Default values as fallback
            self.DEFAULT_AREA = config.get('DEFAULT_AREA', 1000)
            self.DEFAULT_SPEED = config.get('DEFAULT_SPEED', 1)
            self.MAX_SPEED = config.get('MAX_SPEED', 10)
            self.user_contact = config.get('USER_CONTACT', 'Unknown')
            self.security_company_contact = config.get('SECURITY_CONTACT', '999')
                                                       

            # Initialize with default values
            self.__area = self.DEFAULT_AREA
            self.__speed = self.DEFAULT_SPEED
            self.__config_set = False
            self.__current_location = 0

    def check_config(self):
        if not self.__config_set:
            self.input_config()
            self.__config_set = True

    def input_config(self):
        self.__area = self.__get_valid_input('Enter patrol area (Number between 1-5000): ', self.MAX_AREA, self.DEFAULT_AREA)
        self.__speed = self.__get_valid_input('Enter patrol speed (Number between 1-10): ', self.MAX_SPEED, self.DEFAULT_SPEED)

    def __get_valid_input(self, prompt, max_value, default):
        while True:
            try:
                value = int(input(prompt))
                if 0 < value <= max_value:
                    return value
                else:
                    print(f"Value must be between 1 and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def set_area(self, area):
        self.__area = area if 0 < area <= self.MAX_AREA else self.DEFAULT_AREA

    def get_speed(self):
        return self.__speed

    def update_location(self, move_distance):
        self.__current_location = (self.__current_location + move_distance) % self.__area

    @property
    def current_location(self):
        return self.__current_location

    @property
    def max_area(self):
        return self.__area
