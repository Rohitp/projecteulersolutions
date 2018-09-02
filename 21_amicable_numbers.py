from library import findFactors
import time

start = time.time()

factorsDict = {}
amicableNumbers = set()
for x in range(2, 10001):
    factorsDict[x] = sum(list(findFactors(x) - {x}))
    for key in factorsDict:
        if factorsDict[key] == x and key != x and factorsDict[x] == key:
            amicableNumbers = amicableNumbers | { key , x}


print(sum(list(amicableNumbers)))

end = time.time()
print("Time elapsed "+ str(end - start))
