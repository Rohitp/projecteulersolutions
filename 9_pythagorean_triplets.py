import time
start = time.time()


def triplets():
    for a in range(1,999):
        for b in range(a + 1, 999):
            c = 1000 - a - b
            if ((a**2) + (b**2) == (c**2)):
                return (a * b * c)


print(triplets())

end = time.time()
print("Time elapsed "+ str(end - start))