def list_caller(func, params: list):
    return func(*params)

def dict_caller(func, params: list):
    return func(**params)

def printer(name, origin):
    print(f"{name} is from {origin}")

list_caller(printer, ["Moana", "Matanui"])
dict_caller(printer, {'name': "Moana", 'origin': "Matanui"})

func = list_caller
func(printer, ["Moana", "Matanui"])

def get_multiplier():
    def inner(a, b):
        return a * b
    return inner

multiplier = get_multiplier() # multiplier будет содержать функцию inner!
print(multiplier.__name__)
print(type(multiplier))
print(multiplier(3, 5))


def get_specific_multiplier(number):
    def inner(a):
        return a * number
    return inner

multiplier_by_2 = get_specific_multiplier(2)
print(multiplier_by_2(10))

def squarify(a):
    return a ** 2

result = map(squarify, range(5))
print(type(result))
print(list(result))


def is_positive(a):
    return a > 0

result = filter(is_positive, range(-2, 3))
print(type(result))
print(list(result))

result = map(lambda x: x ** 2, range(5))
print(list(result))

func = lambda x: x ** 2
print(type(func))
print(func.__name__)

result = filter(lambda x: x > 0, range(-2, 3))
print(list(result))


def conversion(numbers: list) -> list:
    return list(map(str, numbers))
    #return list(map(lambda number: str(number), numbers))

print(conversion([1, 2, 13, 18]))


from functools import reduce

def multiply(a, b):
    print(f"{a} * {b}")
    return a * b

result = reduce(multiply, [1, 2, 3, 4, 5])
print(result)

result = reduce(lambda x, y: x* y, range(1,6))
print(result)

from functools import partial

def greeter(person, greeting):
    return f"{greeting}, {person}"


hier = partial(greeter, greeting="Hi")
helloer = partial(greeter, greeting="Hello")
yuri_greeter = partial(greeter, person="Yuri")

print(yuri_greeter(greeting='Привет'))
