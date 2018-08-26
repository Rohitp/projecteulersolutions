from math import log, sqrt, ceil
import time


start = time.time()

def nthPrime(n):
    
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 5

    # Consistently overestimates an upper bound. 
    # For small numbers like 100 about 6x bigger. But it gets very efficient at the 10,000 mark or so
    # Which is the point of this
    estimatedUpperLimit = ceil(n * log(n) + n * log(log(n)))
    rootUpperLimit = ceil(sqrt(estimatedUpperLimit)) + 1

    sieve = [True for x in range(estimatedUpperLimit)]

    for x in range(2, rootUpperLimit):
        if(sieve[x]):
            for y in range(x * x, estimatedUpperLimit, x):
                sieve[y] = False

    # I dont want a wasted iteration for these two. Especially for large numbers
    sieve[0] = False
    sieve[1] = False

    count = 0
    for x in range(estimatedUpperLimit):
        if sieve[x]:
            count = count + 1
        if count == n:
            return x
        


print(nthPrime(10001))
            

end = time.time()
print("Time elapsed "+ str(end - start))