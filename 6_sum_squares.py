import time

start = time.time()


# Sum till n = (n * (n+1)) / 2
# Sum of n^2 = (n * (n + 1) * (2*n + 1))/6

def sum_difference(n):
    return int(((n * (n+1)) / 2) ** 2 - ((n * (n + 1) * (2*n + 1))/6))

print(sum_difference(100))

end = time.time()
print("Time elapsed "+ str(end - start))