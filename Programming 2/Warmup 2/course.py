class Course():

    def __init__(self, name, credits):
        self.__name = name
        self.__credits = credits

    def get_credits(self):
        return self.__credits

    def get_name(self):
        return self.__name
