from library import memoize
import time

start = time.time()


# Here we have two solutions.
# One a solution with memoization and one with a greedy approach bottom to top

file = open("67_maximum_path.txt",  "r")
TRIANGLE_MATRIX = []
for line in file:
    TRIANGLE_MATRIX.append(list(map(int, line.split(" "))))

SIZE =  len(TRIANGLE_MATRIX)
greatestPath = 0

memoization = {}

@memoize
def calculatePath(x, y, total):
    global greatestPath
    if x == SIZE:
         if total > greatestPath:
             greatestPath = total

    if x < SIZE:
        if y < len(TRIANGLE_MATRIX[x]):
            calculatePath(x + 1, y + 1, total + TRIANGLE_MATRIX[x][y])

        calculatePath(x + 1, y, total + TRIANGLE_MATRIX[x][y])

    return greatestPath

def calculatePathAddition():
    for x in range(SIZE - 2, -1, -1):
        for y in range(0, len(TRIANGLE_MATRIX[x])):
            if y + 1 < len(TRIANGLE_MATRIX[x]):
                TRIANGLE_MATRIX[x][y] += max(TRIANGLE_MATRIX[x+1][y], TRIANGLE_MATRIX[x+1][y+1])
            else:
                 TRIANGLE_MATRIX[x][y] += TRIANGLE_MATRIX[x+1][y]
    

    return TRIANGLE_MATRIX[0][0]

print(calculatePathAddition())

end = time.time()
print("Time elapsed "+ str(end - start))