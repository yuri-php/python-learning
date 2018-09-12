def test_global_immutable():
    global var_immutable
    var_immutable = 35
    print(f"Local value {var_immutable}")

def test_global_mutable():
    var_mutable.append(4)
    print(f"Local value {var_mutable}")

def split_tags(tag_string: str):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())

    return tag_list

def add(x: int, y: int) -> int:
    return x + y

def extender(source_list: list, extend_list: list):
    source_list.extend(extend_list)

def replacer(source, replace):
    source = replace

def say(greeting, names):
    print(f"{greeting} {names}!")

def default_values_immutable(name="Yuri"):
    print(f"Name is {name}")

def default_values_mutable(professions=[]):
    return professions

def printer(*args):
    print(type(args))

    for argument in args:
        print(argument)

def printer_kv(**key_values):
    print(type(key_values))

    for key, value in key_values.items():
        print(f"{key} - {value}")

def printer_complex(*values, **key_values):
    print("Position arguments")
    for value in values:
        print(value)

    print("Named arguments")
    for key, value in key_values.items():
        print(f"{key} - {value}")


print(split_tags("YSH, AVO, BMA"))
print(add(1, 2))
print(add('a', 'b')) #works!!!!

values = [1, 2, 3]
extender(values, [4, 5, 6])
print(values) #values changed so it was passed by reference

user_info = ['YSH', '22/07']
replacer(user_info, ['OSH', '28/11'])
print(user_info)

user_info = ('YSH', '22/07')
replacer(user_info, ('OSH', '28/11'))
print(user_info)

print(say(names="Юра", greeting="Привет"))

var_immutable = 34
var_mutable = [1, 2, 3]
test_global_immutable()
print(f"Global value {var_immutable}")
test_global_mutable()
print(f"Global value {var_mutable}")

default_values_immutable()
default_values_immutable("Olesya")

profs1 = default_values_mutable()
profs1.append('Teacher')
print(profs1)

profs2 = default_values_mutable()
profs2.append('Doctor')
print(profs2)

print(default_values_mutable.__defaults__)

printer('a', 10)
name_list = ['YSH', 'AVO', 'BMA']
printer(*name_list)

printer_kv(name="YSH", age=39)
employees_dict = {
    'name': 'Yuri',
    'age': 39
}
printer_kv(**employees_dict)

printer_complex(1, 2, name="Yuri")
printer_complex(13)