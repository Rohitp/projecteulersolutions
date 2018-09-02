import time

start = time.time()

# This can be cleaned up nicely but since this is a straight forward problem I don't really care

letterLookup = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40 : 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'
}

sum = 0

def numtoWords(n):
    assert n < 9999, "Only Numbers Till 9999 are supported. For now"
    if n <= 20:
        return letterLookup[n]

    size = len(str(n)) - 1
    i = 0
    words = ''
    while (size >= 0):
        num = int(str(n)[i])
        if num:
            if size == 0 and int(str(n)[i - 1]) == 0:
                words += "and "
            if size == 1:
                nextDigit = int(str(n)[i + 1])
                if len(str(n)) > 2:
                    words += "and "
                if num == 1:
                    return words + letterLookup[int(str(num)+str(nextDigit))]
                else:
                    words += letterLookup[num * 10]+" "
            else:
                words += letterLookup[num] + " "
                if size:
                    words += letterLookup[ 10 ** size ]+" "
        size -= 1
        i += 1
    
    return words.strip()
    
    

for x in range(1, 1001):
    sum += len(numtoWords(x).replace(" ",""))

print(sum)

end = time.time()
print("Time elapsed "+ str(end - start))