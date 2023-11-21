class Config:

    def __init__(self):
        self.__config_set = False
        self.__area = None
        self.__current_location = None
        self.__speed = 1

    def check_config(self):
        if self.__config_set is False:
            self.input_config()
            self.__current_location = self.__area
            self.__config_set = True

    def input_config(self):
        self.set_area( int(input('Enter patrol area (Number between 0-5000): ')))
        self.set_speed( int(input('Enter patrol speed (Number between 1-10): ')))

    def set_area(self, area: int):
        if area >= 5000:
            self.__area = 5000
        elif area < 0:
            self.__area = 0
        else:
            self.__area = area

    def set_speed(self, speed: int):
        if speed > 10:
            self.__speed = 10
        elif speed < 1:
            self.__speed = 1
        else:
            self.__speed = speed

    def get_speed(self):
        return self.__speed

    def get_area(self):
        return self.__area
    
    @property
    def get_current_location(self):
        return self.__current_location
    

    def patrol_location(self, location):
        if self.__current_location <= 0:
            self.__current_location = self.get_max_area
        self.__current_location -= location
    
    def return_to_station(self, location):
        if self.__current_location >= self.get_max_area:
            self.__current_location = self.get_max_area
        self.__current_location += location

    @property
    def get_max_area(self):
        return self.__area
