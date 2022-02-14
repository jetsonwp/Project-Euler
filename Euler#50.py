import bisect
# the variable n limits the primes you calculate to less then or equal to its value.
n = 1000000
# the variable b is the starting index when iterating through the array of prime numbers.
b = 0
prime_numbers = []
#the array prime_sums stores each consecutive prime.
prime_sums = []
testprime_sums = []
#the array prime_lengths store each consecutive primes length.
prime_lengths = []
testprime_lengths = []
prime = [True for i in range(n+1)]
p = 2
#the variable v is a placeholder for the sum of primes.
v = 0
#the variable c is a placeholder for the length of consecutive primes. 
c = 0
while (p * p <=n):
    if (prime[p] == True):
        for i in range(p * p, n+1, p):
            prime[i] = False
    p += 1        
for p in range(2, n+1):
    if prime[p]:
        #appends each prime to a list.
        prime_numbers.append(p)
#The above caculates all the primes to n and then appends them to a list.
#this loop goes through the primes in the array prime_numbers starting at index b and adds them.
while b <= 3:
    for x in prime_numbers[b:]:
        v+=x
        c+=1
        #If the sum is in the array of prime numbers it is appended to a new array of prime sums. The length of consecutive primes is also added to an array.
        if v in prime_numbers:
                #the variable m is the index at which each prime should be inserted into the list
                m = bisect.bisect_right(prime_sums,v)
                prime_sums.insert(m, v)
                prime_lengths.insert(m, c)
                print(m)
                print(v)
                print(testprime_sums)
        if v > n:
            break
    b += 1
    #resets all temporary values
    v = 0 
    x = 0 
    c = 0
print(prime_sums)    
print(prime_lengths)
