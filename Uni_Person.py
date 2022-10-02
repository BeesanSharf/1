class Person:
    def __init__(self, name, age, id):
        self.__name = name
        self.__age = age
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
