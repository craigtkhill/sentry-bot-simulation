class Config:
    MAX_AREA = 5000  # Maximum patrol area in square meters
    MAX_SPEED = 10   # Maximum speed
    MIN_SPEED = 1    # Minimum speed

    def __init__(self):
        self.__config_set = False
        self.__area = 0
        self.__speed = 1
        self.__current_location = 0

    def check_config(self):
        """ Check if configuration is set, otherwise input the configuration """
        if not self.__config_set:
            self.input_config()
            self.__current_location = self.__area  # Assuming starting at one end of the area
            self.__config_set = True

    def input_config(self):
        """ Input configuration from the user """
        try:
            area = int(input('Enter patrol area (Number between 0-5000): '))
            speed = int(input('Enter patrol speed (Number between 1-10): '))
            self.set_area(area)
            self.set_speed(speed)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def set_area(self, area: int):
        """ Set the patrol area """
        if 0 <= area <= self.MAX_AREA:
            self.__area = area
        else:
            print(f"Area should be between 0 and {self.MAX_AREA}. Setting to default (0).")
            self.__area = 0

    def set_speed(self, speed: int):
        """ Set the patrol speed """
        if self.MIN_SPEED <= speed <= self.MAX_SPEED:
            self.__speed = speed
        else:
            print(f"Speed should be between {self.MIN_SPEED} and {self.MAX_SPEED}. Setting to default ({self.MIN_SPEED}).")
            self.__speed = self.MIN_SPEED

    def get_speed(self):
        """ Get the current patrol speed """
        return self.__speed

    def get_area(self):
        """ Get the patrol area """
        return self.__area

    @property
    def current_location(self):
        """ Get the current location of the bot """
        return self.__current_location

    def patrol_location(self, move_distance):
        """ Update the current location during patrolling """
        self.__current_location = (self.__current_location + move_distance) % self.__area

    def return_to_station(self):
        """ Set the current location to the charging station """
        self.__current_location = 0 

    @property
    def max_area(self):
        """ Get the maximum area the bot can patrol """
        return self.__area
