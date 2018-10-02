# I had a much mopre elegant solution to this
# But like problem 24 I lost this one when swithcing laptops
# So we get this one for completeness

from itertools import permutations, count
from library import memoize
import time

start = time.time()


@memoize
def fibonacci(n):
    if n <= 1:
        return 1;
    return fibonacci(n - 1) + fibonacci(n -2)


for i in count(start=1):
    if len(str(fibonacci(i))) >= 1000:
        # +1 here as we ignore 0 in the function
        print(i + 1)
        break;

end = time.time()
print("Time elapsed "+ str(end - start))
