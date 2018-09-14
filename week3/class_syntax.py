class Robot:
    """This class don't do anything too"""


print(Robot)
print(dir(Robot))


class Planet:
    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print('__init__ called')
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"

    def add_human(self, human):
        self.population.append(human)


planet = Planet('Earth')
print(planet.name)
print(planet)


planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Pluto', 'Neptune']
planets = []
for name in planet_names:
    planets.append(Planet(name))


print(planets)
print(planet_names)
print('Mercury')
print(str('Mercury'))
print(repr('Mercury'))
print(str(planet_names))
print(repr(planet_names))


planet = Planet('Alpha')
planet.colour = 'blue'
print(planet.colour)
#del planet.colour
#print(planet.colour) # Exception

class Human:
    def __new__(cls, *args, **kwargs):
        print('__new__ Human called')
        print(super().__class__)
        obj = super().__new__(cls)
        return obj

    def __del__(self):
        print("Bye")


human = Human()
human = 'Yuri'


class Robot:
    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power


wall_e = Robot(100)
wall_e.power = -20
print(wall_e.power)
print(type(wall_e.power))


class Robot:
    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        # здесь могут быть любые полезные вычисления
        return self._power

wall_e = Robot(200)
print(wall_e.power)
wall_e._power = 100
print(wall_e.power)
