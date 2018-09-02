from functools import reduce
import time

start = time.time()

print(sum(list(map(int,list(str(reduce(lambda x, y: x *y, list(range(1,101)))))))))

end = time.time()
print("Time elapsed "+ str(end - start))