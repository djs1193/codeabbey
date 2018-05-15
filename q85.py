import numpy as np
from copy import copy, deepcopy

field = np.empty([12,12], dtype = str)
field[:] = '-'
field[3][3] = "X"                    #5x7 starts from 3,3
field[3][4] = "X"
field[3][6] = "X"
field[3][7] = "X"
field[4][3] = "X"
field[4][4] = "X"
field[4][5] = "X"
field[4][7] = "X"
field[5][3] = "X"
field[5][6] = "X"
field[5][7] = "X"
field[6][3] = "X"
field[6][7] = "X"
field[6][8] = "X"
field[6][9] = "X"
field[7][8] = "X"
field[7][9] = "X"

newfield = deepcopy(field)

print(field)
print(" ")

def neighbor(r,c,field):
    n = 0
    try :
        if (field[r-1][c-1] == "X"):
            n+=1
        if (field[r-1][c] == "X"):
            n+=1
        if (field[r-1][c+1] == "X"):
            n+=1
        if (field[r][c-1] == "X"):
            n+=1
        if (field[r][c+1] == "X"):
            n+=1
        if (field[r+1][c-1] == "X"):
            n+=1
        if (field[r+1][c] == "X"):
            n+=1
        if (field[r+1][c+1] == "X"):
            n+=1
    except IndexError:
        n +=0
    return n

def nextround(newfield,field):
    all_nbrs = np.empty([12,12], dtype = str)
    for i in range(0,12):
        for j in range(0,12):
            n = neighbor(i,j,field)
            all_nbrs[i][j]=str(n)

    for i in range(0,12):
        for j in range(0,12):
            if all_nbrs[i][j] == "3" and field[i][j] != "X":
                    newfield[i][j] = "O"
            elif newfield[i][j] == "X" and (all_nbrs[i][j] == "3" or all_nbrs[i][j] == "2"):
                    newfield[i][j] = "X"
            else:
                    newfield[i][j] = "-"
    for i in range(0,12):
        for j in range(0,12):
            if newfield[i][j] == "O":
                newfield[i][j] = "X"


    return(newfield)
    print(" ")



newfield = (nextround(newfield,field))
print(newfield)
c = 0
for i in range(0,12):
    for j in range(0,12):
        if newfield[i][j] == "X":
            c+=1
print(c)
field = deepcopy(newfield)

newfield = (nextround(newfield,field))
print(newfield)
c = 0
for i in range(0,12):
    for j in range(0,12):
        if newfield[i][j] == "X":
            c+=1
print(c)
field = deepcopy(newfield)

newfield = (nextround(newfield,field))
print(newfield)
c = 0
for i in range(0,12):
    for j in range(0,12):
        if newfield[i][j] == "X":
            c+=1
print(c)
field = deepcopy(newfield)

newfield = (nextround(newfield,field))
print(newfield)
c = 0
for i in range(0,12):
    for j in range(0,12):
        if newfield[i][j] == "X":
            c+=1
print(c)
field = deepcopy(newfield)

newfield = (nextround(newfield,field))
print(newfield)
c = 0
for i in range(0,12):
    for j in range(0,12):
        if newfield[i][j] == "X":
            c+=1
print(c)
