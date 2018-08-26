import time

start = time.time()

# Memoization reduces the runtime from an average of 50 seconds to 4 seconds
memoization = { 1: 1}

def collatz(n, count = 1):
    if n == 1:
        return count

    if n in memoization:
        return count + memoization[n]

    if not n & 1:
        return collatz(int(n/2), count+1)
    else:
        return collatz( (3 * n) + 1, count+1)
       



maxLength = 0
collatzMaxSeed = 0
for x in range(1, 1000001):
    length = collatz(x)
    if length > maxLength:
        maxLength, collatzMaxSeed = length, x
      
    if x not in memoization:
       memoization[x] = length
           

print(collatzMaxSeed)

end = time.time()
print("Time elapsed "+ str(end - start))