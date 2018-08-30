import time

start = time.time()

# Using pythons arbitary precision lntegers makes this as trivial as 
# print(sum(list(map(int, list(str(math.pow(2, 1000))))))
# We're going to do it like we'd do it in c


def sumPow(base, power):

    power = power + 1
    number = [0 for x in range(power)]
    # 2 ** 0 = 1
    number[0] = 1
    limit = 1
    for coef in range(1, power):
        carry = 0
        digit = 0
        while digit < limit:
            value = (number[digit] * base) + carry
            num = value % 10
            number[digit] = num 
            digit = digit + 1
            carry = 0
            if (value > 9):
                carry = int(value/10)
        limit = limit + 1

    return sum(number)

print(sumPow(2, 1000))

end = time.time()
print("Time elapsed "+ str(end - start))