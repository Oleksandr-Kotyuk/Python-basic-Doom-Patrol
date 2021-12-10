# 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


# 3
new_bus = Bus(85, 18000, 180)
print(type(new_bus))
# <class '__main__.Bus'>

# 4
school_bus = Bus(90, 23000, 200)
print(isinstance(school_bus, Vehicle))
# True

# 5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, capacity, bus_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, capacity)
        self.bus_color = bus_color

    def bus_school_color(self):
        print(f'Bus color is {self.bus_color}')


# 7
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (self.sound)


class Wolf(Bear):
    def __init__(self, sound):
        super().__init__(sound)


bears = Bear('Brr-rr')
wolves = Wolf('Auf')
animals = (bears, wolves)

for sound in animals:
    print(sound.make_sound())


# 8
class City:
    def __new__(cls, name, population):
        if population < 1500:
            return "Your city is too small"
        return object.__new__(cls)

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def population(self):
        return self.population


lviv = City('Lviv', 670000)
kovel = City('Kovel', 650)
dnipro = City('Dnipro', 1127000)

cities = (lviv, kovel, dnipro)

for el in cities:
    print(el)
