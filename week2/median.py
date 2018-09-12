import random

numbers =  []
size = random.randint(10, 15)

for _ in range(size):
    numbers.append(random.randint(10, 20))

print(numbers)
numbers.sort()
print(numbers)

numbers_len = len(numbers)
print(f"Len is {numbers_len}")

middle_position = len(numbers) // 2
print(f"Median index is {middle_position}")
median = None
if numbers_len % 2 == 1:
    median = numbers[middle_position]
elif numbers_len > 0:
    median = (numbers[middle_position] + numbers[middle_position - 1]) / 2
    #median = sum(numbers[middle_position - 1:middle_position + 1]) / 2

print(f"Median is {median}")

import statistics

print(statistics.median(numbers))

