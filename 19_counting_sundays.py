from math import floor
import time

start = time.time()

# Formula from https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
# W = ( k + floor(2.6*m - 2) -2*C + y + floor(y/4) + floor(C/4) ) % 7
# k is day (1 to 31)
# m is month (1 = March, ..., 10 = December, 11 = Jan, 12 = Feb) Treat Jan & Feb as months of the preceding year
# C is century (1987 has C = 19)
# Y is year (1987 has Y = 87 except Y = 86 for Jan & Feb)
# W is week day (0 = Sunday, ..., 6 = Saturday)



def findDay(m, y, k, C = 19):
    return ( k + floor(2.6*m - 2) -2*C + y + floor(y/4) + floor(C/4) ) % 7


sundays = 0
monthSizeArray = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28]
for y in range(1, 100):
    for  m in range(1, 13):
        monthLength = monthSizeArray[m -1]
        if y % 4 == 0 and m == 12:
            monthLength = 29
        for d in range(1, monthLength + 1):
            if m > 10:
                weekday = findDay(m, y -1, d)
            else:
                weekday = findDay(m , y, d)
            if weekday == 0 and d == 1:
                sundays += 1

# Jan and feb of the next year. Too bored to make this more efficient
for m in range(11, 13):
    for d in range(1, monthSizeArray[m -1]):
        weekday = findDay(m, 99, d)
        if weekday == 0 and d == 1:
            sundays += 1



print(sundays)
end = time.time()
print("Time elapsed "+ str(end - start))
