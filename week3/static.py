from datetime import date

class Planet:
    count = 0  # Переменная класса, а не объекта - то есть статическая переменная

    def __init__(self, name):
        self.name = name
        Planet.count += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"


planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Pluto', 'Neptune']
planets = []
for name in planet_names:
    planets.append(Planet(name))

print(Planet.count)
alpha = Planet('Alpha')
print(alpha.count)

alpha.count = 13
print(alpha.count)
print(Planet.count)


def extract_description(user_string):
    return "открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)



class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)


event_description = "Рассказать, что такое @classmethod"
event_date = date.today()
event = Event(event_description, event_date)
print(event)

event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150
