import time
from math import sqrt, ceil
start = time.time()

# Since we're trying to find the factor for a specific number this
# is not a genericized solution. We don't consider 2 and if the number itself is prime.

n = 600851475143
greatestFactor = 3;

for x in range (3, ceil(sqrt(n)), 2):
    while not n % x:
        greatestFactor = x
        n = ceil(n/x)
        
        
    
print(greatestFactor)
end = time.time()
print("Time elapsed "+ str(end - start))