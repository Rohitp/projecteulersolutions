from math import ceil, sqrt

def findPrimefactors(n):  

    # Storing it here for prime case. Must be a better way to do this. 
    # But I have a time limit of 10 minutes for each problem before 20 and I don't care
    number = n;
    factors = {}

    while not n % 2:
        factors[2] = factors.get(2,0) + 1
        n = n/2
         
    n = number     
    for x in range(3, (ceil(sqrt(n)) + 2), 2):
        while not n % x:
            factors[x] = factors.get(x,0) + 1
            n = n/x

    if not factors:
        factors[number] = 1

    return factors
        

print(findPrimefactors(100))
    
