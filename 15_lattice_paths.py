from library import Memoize
import time

start = time.time()

@Memoize
def traverseGrid(x, y, iterations):
    if x == 0 and y == 0:
        # Path has been reached through some mechanism
        return 1

    count = 0

    if x > 0:
        count += traverseGrid(x-1, y, iterations + 1)    

    if y > 0:
        count +=traverseGrid(x, y-1, iterations + 1)
 
    return count

print(traverseGrid(20 ,20, 1))

end = time.time()
print("Time elapsed "+ str(end - start))
