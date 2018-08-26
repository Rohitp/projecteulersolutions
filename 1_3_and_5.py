import time
start = time.time()

sumMultiples = sum([x for x in range(1000) if x%3 == 0 or x%5 == 0 ])
print(sumMultiples)

end = time.time()
print("Time elapsed "+ str(end - start))