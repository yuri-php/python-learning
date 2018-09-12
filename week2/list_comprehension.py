square_list = [number * 2 for number in range(10)[1:5]]
print(square_list)

even_list = [num ** 2 for num in range(10) if num % 2 == 0]
print(even_list)

square_map = {str(number): number ** 2 for number in range(5)}
print(square_map)

reminder_set = {number % 10 for number in range(100)}
print(reminder_set)

print(type(number * 2 for number in range(10)[1:5]))
print(type(number % 10 for number in range(100)))

num_list = range(7)
squared_list = [x ** 2 for x in num_list]
print(list(zip(num_list, squared_list)))
