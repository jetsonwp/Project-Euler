# the value of x determines the how many Fibonacci numbers will be calculated
x = 10000
# initial value
q = 0
# second value
w = 1
# placeholder
e = 0

for i in range(x):
    e = q + w
    q = w
    w = e
    if len(str(e)) == 1000:
        print(e, i + 2)
        break