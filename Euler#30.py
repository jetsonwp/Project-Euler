x = 10000000
w = 0
for i in range(1, x + 1):
    z = str(i)
    for c in range(0, len(z)):
        v = int(z[c])
        w += v ** 5
    if i == w:
        print(i, w)
    w = 0

