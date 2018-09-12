import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print("Уравнение не имеет решения")
    exit(1)

divisor = 2 * a
x1 = (-b - discriminant ** 0.5) / divisor #math.sqrt
x2 = (-b + discriminant ** 0.5) / divisor

print(int(x1))
print(int(x2))
