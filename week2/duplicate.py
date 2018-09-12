import random

random_set = set()
iterations_number = 0
while True:
    iterations_number += 1
    rand_value = random.randint(1, 10)
    if rand_value in random_set:
        break

    random_set.add(rand_value)

print(f"Повтор произошел на {iterations_number} итерации. Повторившееся число {rand_value}")
other_way_iterations_number = len(random_set) + 1
print(f"Повтор произошел на {other_way_iterations_number} итерации. Повторившееся число {rand_value}")