from math import log, sqrt, ceil
import time


start = time.time()

# Reusing the same sieve function instead of proper package management cause I'm lazy

def sumPrimes(n):
    
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 5

    # Here it's the same as problem 7 except I replace the upper limit from an estomate range to the number itself 
    estimatedUpperLimit = n
    rootUpperLimit = ceil(sqrt(estimatedUpperLimit)) + 1

    sieve = [True for x in range(estimatedUpperLimit)]

    for x in range(2, rootUpperLimit):
        if(sieve[x]):
            for y in range(x * x, estimatedUpperLimit, x):
                sieve[y] = False

    # I dont want a wasted iteration for these two. Especially for large numbers
    sieve[0] = False
    sieve[1] = False

    sum = 0
    for x in range(estimatedUpperLimit):
        if sieve[x]:
            sum += x
        if x == n - 1:
            return sum


print(sumPrimes(2000000))
            

end = time.time()
print("Time elapsed "+ str(end - start))   