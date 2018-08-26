import time
start = time.time()

def findPalindrome():
    pal = 0
    for x in range(999, 100, -1):
        for y in range(x, 100,-1):
            if str(x * y) == ''.join(reversed(str(x*y))):
                if(x * y) > pal:
                    pal = x * y
    return pal

print(findPalindrome())

end = time.time()
print("Time elapsed "+ str(end - start))