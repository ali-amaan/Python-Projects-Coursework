import random


class Customer:
    def __init__(self, name):
        self.__name = name
        self.__id = random.randint(1000000, 9999999)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
