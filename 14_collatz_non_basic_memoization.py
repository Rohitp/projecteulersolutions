from library import memoization
import time

start = time.time()

# Here we use memoization using  python class. I added both solutions. This gets too language specific and is a simple exercise for my own understanding.

        

@memoization
def collatz(n, count):
    if n == 1:
        return count

    if not n & 1:
        return collatz(int(n/2), count+1)
    else:
        return collatz( (3 * n) + 1, count+1)
       



maxLength = 0
collatzMaxSeed = 0
for x in range(1, 1000001):
    length = collatz(x, 1)
    if length > maxLength:
        maxLength, collatzMaxSeed = length, x
      
           

print(collatzMaxSeed)

end = time.time()
print("Time elapsed "+ str(end - start))