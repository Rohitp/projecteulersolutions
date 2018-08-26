from math import ceil, sqrt
from functools import reduce
import time

start = time.time()

#  For this problem I refuse to use python inbuilt gcd class
# So we use the formula lcm(a,b,c,...n) - lcn(lcm(lcm(a,b),c)...n)
# a * b = gcd * lcm


def findFactors(n):  

    # Using a set here for perfect squares like 100 not returning the factors twice
    return set(reduce(lambda a,b: a+b, [[x, int(n/x)] for x in range(1, (ceil(sqrt(n)) + 1)) if not n%x]))

def gcd(a, b):
    return max(sorted(findFactors(a).intersection(findFactors(b))))

def lcm(a,b):
    return (a*b)/gcd(a,b)

multiple = 111

# Using 11 to 20 because 1 to 10 is irrelevant as all multiples are evident in 11 to 20
for i in range(11, 20):
    multiple = lcm(multiple, i+1)


print(int(multiple))

end = time.time()
print("Time elapsed "+ str(end - start))
    
