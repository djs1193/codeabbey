import copy



def search(x,y, mazeList):
    # returns True if it has found end of maze
    if mazeList[x][y] == 'F':
        mazeList[x][y] = 'P'
        return True
    elif mazeList[x][y] == 0:
        return False
    elif mazeList[x][y] == 'C':
        return False
    mazeList[x][y] = 'C'
    if (x < rows -1 and search(x+1,y,mazeList)) or (y > 0 and search(x,y-1,mazeList)) or (x > 0 and search(x-1, y,mazeList)) or (y < cols -1 and search(x, y+1,mazeList)):
        mazeList[x][y] = 'P'
        return True
    return False

mylist = [
[1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
[1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0],
[1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1],
[1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0],
[1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1],
[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
[1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1],
[1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0],
[1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1],
[1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
[1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1],
[1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
[1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
[1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
[1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1]
]

mylist[0][0] = 'F'

mylist1 = copy.deepcopy(mylist)
mylist2 = copy.deepcopy(mylist)


rows = 19
cols = 35
search(0,cols-1,mylist)
search(rows-1,0,mylist1)
search(rows-1,cols-1,mylist2)

import numpy as np
np.set_printoptions(linewidth = np.nan,threshold=np.inf)

xarr = []
yarr = []
for i in range(0,rows):
    for j in range(0,cols):
        if mylist[i][j] =='P':
            xarr.append(i)
            yarr.append(j)
maze = np.empty([rows,cols], dtype = "<U10")

for i in range(0,len(xarr)):
    maze[xarr[i]][yarr[i]] = "x"
for i in range(0,rows):
    for j in range(0,cols):
        if maze[i][j] != 'x':
            maze[i][j] = '-'
print(maze)
print(" ")


xarr = []
yarr = []
for i in range(0,rows):
    for j in range(0,cols):
        if mylist1[i][j] =='P':
            xarr.append(i)
            yarr.append(j)
maze1 = np.empty([rows,cols], dtype = "<U10")
for i in range(0,len(xarr)):
    maze1[xarr[i]][yarr[i]] = "x"
for i in range(0,rows):
    for j in range(0,cols):
        if maze1[i][j] != 'x':
            maze1[i][j] = '-'
print(maze1)
print(" ")

xarr = []
yarr = []
for i in range(0,rows):
    for j in range(0,cols):
        if mylist2[i][j] =='P':
            xarr.append(i)
            yarr.append(j)
maze2 = np.empty([rows,cols], dtype = "<U10")
for i in range(0,len(xarr)):
    maze2[xarr[i]][yarr[i]] = "x"
for i in range(0,rows):
    for j in range(0,cols):
        if maze2[i][j] != 'x':
            maze2[i][j] = '-'
print(maze2)
