numbers = []
x = 0
z = 0
c = 100
q = 0
s = 0
d = 0
for x in range(1, c + 1):
    for i in range(1, x + 1):
        z += i
    for q in range(1, z + 1):
        if z % q == 0:
            numbers.append(q)
    if len(numbers) > s:
        s = len(numbers)
        d = z
    numbers.clear()
    z = 0
    if s >= 501:
        break
print("Total divisors:", s)
print("Triangle number:", d)