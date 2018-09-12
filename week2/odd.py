odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set)
print(even_set)

union_set = odd_set | even_set
print(union_set)
union_set = odd_set.union(even_set)
print(union_set)

intersection_set = odd_set & even_set
print(intersection_set)
intersection_set = odd_set.intersection(even_set)
print(intersection_set)

difference_set = odd_set - even_set
print(difference_set)
difference_set = odd_set.difference(even_set)
print(difference_set)


symmetric_difference_set = odd_set ^ even_set
print(symmetric_difference_set)
symmetric_difference_set = odd_set.symmetric_difference(even_set)
print(symmetric_difference_set)

odd_set.remove(1)
print(odd_set)