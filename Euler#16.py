# sum of the integers of z
w = 0
# initial value of what is being factored
x = 2
# value of the factor
n = 1000
# the factored value of x
z = str(x ** n)
print(z)
sumValue = 0
for digit in z:
    sumValue += int(digit)
print(sumValue)