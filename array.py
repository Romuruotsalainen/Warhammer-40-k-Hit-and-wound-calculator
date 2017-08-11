import numpy

newArray = numpy.zeros((10, 10))
for t in range(8):
    for i in range(8):
        newArray[t + 2][0 + t - i] = 2

for i in range(9):
    newArray[i + 1][i] = 3

for i in range(10):
    newArray[i][i] = 4
    
for i in range(9):
    newArray[i][i + 1] = 5

for i in range(8):
    newArray[i][i + 2] = 6

for i in range(7):
    newArray[i][i + 3] = 6

for i in range(6):
    newArray[i][i + 4] = None

for i in range(5):
    newArray[i][i + 5] = None

for i in range(4):
    newArray[i][i + 6] = None

for i in range(3):
    newArray[i][i + 7] = None

for i in range(2):
    newArray[i][i + 8] = None

newArray[0][9] = None

print(newArray)
