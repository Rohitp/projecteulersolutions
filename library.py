from math import ceil, sqrt, log
from functools import reduce

# Input - number n
# Output the factors of the number n in a set
# 10 -> {1, 10, 2, 5}

def findFactors(n):  

    # Using a set here for perfect squares like 100 not returning the factors twice
    return set(reduce(lambda a,b: a+b, [[x, int(n/x)] for x in range(1, (ceil(sqrt(n)) + 1)) if not n%x] ))




# returns the nth prime
# Input number - n
# Output prime corresponsong to the index
# 10 -> 29
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

# Used for decorator based memoization - @memoization
# More reading about positional and non positional arguments here
# https://medium.com/@nkhaja/memoization-and-decorators-with-python-32f607439f84

def memoization(f):
    memoize = {}

    def helper(x, y):
        if x not in memoize:
            memoize[x] = f(x, y)
        return memoize[x]
    return helper

class Memoize:
    def __init__(self, func):
        self.func = func
        self.memoize = {}
    def __call__(self, *args):
        if args not in self.memoize:
            self.memoize[args] = self.func(*args)
        return self.memoize[args]