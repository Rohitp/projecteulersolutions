# I solves this without using the python permutations library
# But like a dumbass I forgot to push it to remote when I switched to a new system,
# It used generators
# So we get this for completeness

from itertools import permutations
import time

start = time.time()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("".join(list( permutations(list(map(str, numbers))))[999999]))

end = time.time()
print("Time elapsed "+ str(end - start))
