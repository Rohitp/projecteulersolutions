letterLookup = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3
}

sum = 0
for x in range(1, 6):
    sum = sum + letterLookup[x]

print(sum) 