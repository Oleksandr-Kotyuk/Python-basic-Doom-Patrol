import dataclasses
from collections import namedtuple


# 1
class Laptop:
    def __init__(self):
        battery_1 = Battery('Battery model - A32-K55')
        battery_2 = Battery('Battery model - AS07A51')
        self.batteries = [battery_1, battery_2]


class Battery:
    def __init__(self, model):
        self.model = model


laptop = Laptop()
print(laptop.batteries[0].model)
print(laptop.batteries[1].model)


# 2
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string = GuitarString()
guitar = Guitar(guitar_string)


# 3
class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


print(Calc.add_nums(1, 2, 3))


# 4
# pass


# 5
# pass


# 6
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7
Address_Book_Data_Class = namedtuple('Adress_Book_Data_Class',
                                     ['key',
                                      'name',
                                      'phone_number',
                                      'address',
                                      'email',
                                      'birthday',
                                      'age'])


# 8
class Adress_Book:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return (f'Address_Book(key={self.key}, name={self.name}, '
                f'phone_number={self.phone_number}, address={self.address},'
                f'email={self.email}, birthday={self.birthday}, '
                f'age={self.age})')


# 9
class Person:
    name = "John"
    age = 36
    country = "USA"


my_person = Person()
setattr(my_person, 'age', 22)
print(my_person.age)


# 10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


my_student = Student(17, "Oleksandr")
setattr(my_student, 'email', 'oleksandr@gmail.com')
print(getattr(my_student, 'email'))


# 11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def converter(self):
        return self._temperature * 1.8 + 32


temperature_today = Celsius(45)
print(temperature_today.converter)

