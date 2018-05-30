import numpy as np

game = np.empty([4,4], dtype = "<U10")

game[0,0] = 2
game[0,1] = 2
game[0,2] = 2
game[0,3] = 2
game[1,0] = 4
game[1,1] = 4
game[1,2] = 4
game[1,3] = 4
game[2,0] = 4
game[2,1] = 2
game[2,2] = 2
game[2,3] = 4
game[3,0] = 2
game[3,1] = 2
game[3,2] = 2
game[3,3] = 4

print(game)
print(" ")
move = 'D L L D L L U D U D'.split()

def down(matrix):
    for i in range(2,-1,-1):
        for j in range(0,4):
            if matrix[i+1,j] == matrix[i,j] and matrix[i+1,j]!= '-':
                matrix[i+1,j] = str(int(matrix[i+1,j])*2)
                matrix[i,j] = "-"
    for j in range(0,4):
        array = []
        c = 0
        for i in range(0,4):
            if matrix[i][j] != "-":
                array.append(matrix[i][j])
            else:
                c +=1
        for num in range(0,c):
            array.insert(0,'-')
        for i in range(0,4):
            matrix[i][j] = array[i]
    return(matrix)


def up(matrix):
    for i in range(1,4):
        for j in range(0,4):
            if matrix[i-1,j] == matrix[i,j] and matrix[i-1,j]!= '-':
                matrix[i-1,j] = str(int(matrix[i-1,j])*2)
                matrix[i,j] = "-"
    for j in range(0,4):
        array = []
        c = 0
        for i in range(0,4):
            if matrix[i][j] != "-":
                array.append(matrix[i][j])
            else:
                c +=1
        for num in range(0,c):
            array.append('-')
        for i in range(0,4):
            matrix[i][j] = array[i]

    return(matrix)

def right(matrix):
    for j in range(2,-1,-1):
        for i in range(0,4):
            if matrix[i,j+1] == matrix[i,j] and matrix[i,j+1]!= '-':
                matrix[i,j+1] = str(int(matrix[i,j+1])*2)
                matrix[i,j] = "-"
    for i in range(0,4):
        array = []
        c = 0
        for j in range(0,4):
            if matrix[i][j] != "-":
                array.append(matrix[i][j])
            else:
                c +=1
        for num in range(0,c):
            array.insert(0,'-')
        for j in range(0,4):
            matrix[i][j] = array[j]
    return(matrix)

def left(matrix):
    for j in range(1,4):
        for i in range(0,4):
            if matrix[i,j-1] == matrix[i,j] and matrix[i,j-1]!= '-':
                matrix[i,j-1] = str(int(matrix[i,j-1])*2)
                matrix[i,j] = "-"
    for i in range(0,4):
        array = []
        c = 0
        for j in range(0,4):
            if matrix[i][j] != "-":
                array.append(matrix[i][j])
            else:
                c +=1
        for num in range(0,c):
            array.append('-')
        for j in range(0,4):
            matrix[i][j] = array[j]
    return(matrix)


for i in move:
    if i == 'D':
        var = down(game)
    if i == 'U':
        var = up(game)
    if i == 'R':
        var = right(game)
    if i == 'L':
        var = left(game)
    game = var
    print(game)
    print(" ")

numbers = []
for i in range(0,4):
    for j in range(0,4):
        if game[i][j] != '-':
            numbers.append(int(game[i][j]))
numbers.sort()
unique = set(numbers)
unique = sorted(unique)

m = min(unique)
put = 2

while put not in unique:
    unique.insert(0,put)
    put = put**2

for num in unique:
    print(numbers.count(num))
    print(" ")
