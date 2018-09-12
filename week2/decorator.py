import functools

def decorator(func):
    return func

@decorator # синтаксис декоратора - его название
def decorated():
    print('Hello!')

def decorator(func):
    def new_func():
        pass
    return new_func

@decorator
def decorated():
    print('Hello!')

decorated()
print(decorated.__name__)


def stringify(func):
    return str(func)

@stringify
def multiply(a, b):
    return a * b

#print(multiply(10,2)) # error str() - это строка, а не функция, не callable

def logger(func):
    def wrapped(num_list): #decorated, inner, etc.
        result = func(num_list)
        with open('_log.txt', 'a') as f:
            f.write(str(result) + str(num_list) + "\n")

        return result
    return wrapped


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kvargs): #decorated, inner, etc.
        result = func(*args, **kvargs)
        with open('_log.txt', 'a') as f:
            f.write(str(result) + "\n")

        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

print(summator.__name__)
print(summator([1, 2, 3, 4, 5]))


def complex_logger(filename):
    print(111)
    def decorator(func):
        print(112)
        @functools.wraps(func)
        def wrapped(*args, **kvargs):  # decorated, inner, etc.
            print(113)
            result = func(*args, **kvargs)
            with open(filename, 'w') as f:
                f.write(str(result) + "\n")

            return result
        return wrapped
    return decorator


@complex_logger('_log2.txt')
def complex_summator(num_list):
    print(11)
    return sum(num_list)

print(1)
print(complex_summator.__name__)
print(2)
print(complex_summator([1, 2, 3, 4, 5]))
print(3)


def first_decorator(func):
    print('a1')
    def first_wrapped():
        print('b1')
        print('Inside first_decorator product')
        return func()
    return first_wrapped

def second_decorator(func):
    print('a2')
    def second_wrapped():
        print('b2')
        print('Inside second_decorator product')
        return func()
    return second_wrapped

@first_decorator
@second_decorator
def decorated():
    print('c1')
    print('Finally called...')
# decorated = first_decorator(second_decorator(decorated))
# result = second_wrapped(first_wrapped())
decorated()


def bold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

def italic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@bold
@italic
def hello():
    return "hello world"

# hello = bold(italic(hello))
print(hello())