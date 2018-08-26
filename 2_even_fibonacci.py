import time
start = time.time()

def generateFibonacci():
    a = 0
    b = 1
    while 1:
        temp = a
        a = b
        b = b + temp
        yield b

fibonacciGenerator = generateFibonacci()

sum = 0
for x in fibonacciGenerator:
    if x > 4000000:
        break;
    if x % 2 == 0:
        sum = sum + x
print(sum)    

end = time.time()
print("Time elapsed "+ str(end - start))

    
