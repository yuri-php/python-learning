import sys

digit_string = sys.argv[1]

sum = 0
for symbol in digit_string:
    number = int(symbol)
    sum += number

print(sum)