from library import findFactors
from itertools import count
import time

start = time.time()

# Library is used to reuse functions from previous problems. It's not a python built in.
# I use the same function as from the 5th problem
# Using count from itertools for the infinite loop without using while
# Because while loops look ugly

def getTriangeNumber():
    # Each triangle number is just the sum of numbers untill that.
    # N * (N + 1) /2
    return ( int((x * (x + 1))/2) for x in count(1,1) )

triangleNumbers = getTriangeNumber()


for x in triangleNumbers:
    # Using set.__len__() because len() for sets is slightly expensive
    # Won't really impact performance that much but whatever
    if findFactors(x).__len__() > 500:
        print(x)
        break


end = time.time()
print("Time elapsed "+ str(end - start))