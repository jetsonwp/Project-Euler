from itertools import permutations
x = 0
numbers = permutations("0123456789")
for j in list(numbers):
    x += 1
    if x == 1000000:
        print(j)
        break
