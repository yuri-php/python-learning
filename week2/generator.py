def even_range(start, end):
    current = start
    while current < end:
        print('before yield')
        yield current # is like 'return'
        print('after yield') # is executed during NEXT iteration
        current += 2

print(list(even_range(2, 8)))


ranger = even_range(0, 4)
print(next(ranger))
print(next(ranger))

def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

print('fibonacci')
fibonacci_values = fibonacci(10)
print(type(fibonacci_values))
print(dir(fibonacci_values))
print(next(fibonacci_values))
print(next(fibonacci_values))
print(next(fibonacci_values))
print(next(fibonacci_values))
print(next(fibonacci_values))

for i in fibonacci(10):
    print(i)

print('Generator values')
def accumulator():
    total = 0
    while True:
        value = yield total
        print(f"Got {value}")

        if not value:
            print('Generation finished')
            break
        total += value

generator = accumulator()
print(next(generator))
print(generator.send(3))
print(generator.send(5))
#print(next(generator)) # value will be None

print('Generator values in cycle')
generator = accumulator()
next(generator)
for i in range(4)[1:]:
    print(generator.send(i))
