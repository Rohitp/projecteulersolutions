from functools import reduce
import time

start = time.time()

file = open("22_name_scores.txt", "r")
names = []

# He we don't bother converting to uppercase as we assume the input is sanitized

for line in file:
    names.extend(line.replace('"',"").split(","))

names.sort()

score = sum([ x * (i+1) for i,x in enumerate(list(map(lambda x: reduce(lambda c, d: (ord(c) - 64) + (ord(d) - 64) if not isinstance(c, int) else c + (ord(d) - 64), list(x)) , names))) ])


print(score)

end = time.time()
print("Time elapsed "+ str(end - start))