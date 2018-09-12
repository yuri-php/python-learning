import random

example_num = random.randint(0, 101)
user_num = None

while user_num != example_num:
    user_num = input("Введите число: ")
    if user_num is "" or user_num == "exit":
        break

    if not user_num.isdigit():
        print("Это не натуральное число")
        continue

    user_num = int(user_num)
    if user_num < example_num:
        print("Число больше")
    elif user_num > example_num:
        print("Число меньше")
    else:
        print("Вы угадали")
        break
