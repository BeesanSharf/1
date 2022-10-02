from Uni_Person import Person


class Employee(Person):
    def __init__(self, salary, name, age, id):
        super().__init__(name=name, age=age, id=id)
        self.__salary = salary

    def get_name(self):
        return str(self.__name).upper()


class Student(Person):
    def __init__(self, number, name, age, id):
        super().__init__(name, age, id)
        self.__number = number

    def get_name(self):
        return str(self.__name).lower()
