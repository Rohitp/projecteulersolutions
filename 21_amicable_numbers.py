from library import findFactors
import time

start = time.time()

factorsDict = {}
amicableNumbers = set()
for x in range(2, 10001):
    sumx = sum(list(findFactors(x) - {x}))
    if (sum(list(findFactors(sumx) - {sumx}))) == x:
        amicableNumbers | {x, sumx}


print(sum(list(amicableNumbers)))

end = time.time()
print("Time elapsed "+ str(end - start))
