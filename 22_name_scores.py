from functools import reduce
import time

start = time.time()
# This is an exercise in making a one liner. Readability de damned
# The input file is a single line containing a csv of names
# He we don't bother converting to uppercase as we assume the input is sanitized

print(sum([ x * (i+1) for i,x in enumerate(list(map(lambda x: reduce(lambda c, d: (ord(c) - 64) + (ord(d) - 64) if not isinstance(c, int) else c + (ord(d) - 64), list(x)) , sorted(open("22_name_scores.txt", "r").readline().replace('"',"").split(",")) ))) ]))

end = time.time()
print("Time elapsed "+ str(end - start))