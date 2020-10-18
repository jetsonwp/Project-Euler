import string
my_file = open("p022_names.txt", 'r')
for line in my_file.readlines():
    my_file = line.rstrip().split(',')
my_file.sort()
str = ""
str1 = my_file
str.join(str1)
values = dict()
# letter sums
z = 0
# word sums
x = 0
# total sums
c = 0
# assigns a value for each letter in the alphabet
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 1
# i is the index of the current word
for i in range(len(my_file)):
    # j is the index of the current letter
    for j in range(1, len(str1[i]) - 1):
        z += values[str1[i][j]]
    x = z * (i + 1)
    c += x
    print(z, i + 1, x)
    z = 0
print(c)