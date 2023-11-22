class Config:
    MAX_AREA = 5000
    DEFAULT_AREA = 1000

    def __init__(self):
        self.__config_set = False
        self.__area = self.DEFAULT_AREA
        self.__speed = 1
        self.__current_location = 0

    def check_config(self):
        if not self.__config_set:
            self.input_config()
            self.__config_set = True

    def input_config(self):
        try:
            area = int(input('Enter patrol area (Number between 0-5000): '))
            self.set_area(area)
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
