# value of n!
x = 100
# product of n!
z = x
# sum of the integers of the product of n!
w = 0
# calculates the product of n!
for c in range(x - 1, 1, -1):
    z *= c
    print(z)
# splits the product of n! into separate integers and puts them into a list
numbers = [int(i) for i in str(z)]
# Calculates the sum of the integers in the list
for q in range(len(numbers)):
    w += numbers[q]
print(w)
