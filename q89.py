import numpy as np
field = np.empty([15,19], dtype = "<U10")
field[:] = '+'

 # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
#0 @ + + + + + + + + + +  +  +  +  +  +  +  +  +
#1 + + + + + + + + + + +  +  +  +  +  +  X  X  +
#2 + + + + + + X + + + +  +  +  X  +  +  +  +  +
#3 + + + + X X X + + + +  +  +  +  +  +  X  +  +
#4 + X + + X + + + + + X  +  +  X  X  +  +  +  +
#5 + X + + X + + + + + X  +  +  +  +  +  +  +  X
#6 + + + + + + + + + + +  +  +  +  +  +  +  +  +
#7 + + X + + + + + + + +  X  X  +  +  +  +  +  +
#8 + + + + + + + + + + +  +  X  +  +  +  +  +  +
#9 + + + + + + + + + + X  +  +  +  +  +  +  X  +
#10+ + + + + + X + + X +  +  +  X  +  +  X  +  +
#11+ + + + + + + X X + +  +  +  +  X  +  X  +  X
#12+ + + + + + + + + + +  X  +  +  +  +  +  +  +
#13+ X + + + + X + + + +  +  +  +  +  +  +  +  +
#14+ + + X + + + + + + X  +  +  +  +  +  +  +  $

field[1][16] = field[1][17] = field[2][6] = field[2][13] = field[3][4] = field[3][5] = '0'
field[3][6]  = field[3][16] = field[4][1] = field[4][4] = field[4][10] = field[4][13] = '0'
field[4][14] = field[5][1] = field[5][4] = field[5][10] = field[5][18] = field[7][2] = '0'
field[7][11] = field[7][12] = field[8][12] = field[9][10] = field[9][17] = field[10][6] = '0'
field[10][9] = field[10][13] = field[10][16] = field[11][7] = field[11][8] = field[11][14] = '0'
field[11][16] = field[11][18] = field[12][11] = field[13][1] = field[13][6] = field[14][3] = '0'
field[14][10] = '0'

for i in range(0,15):
    if field[i][0] != "0":
        field[i][0] = "1"

for j in range(0,19):
    if field[0][j] != "0":
        field[0][j] = "1"



print(field)

for i in range(1,15):
    for j in range(1,19):
        if field[i][j] != '0':
            field[i][j] = int(field[i - 1][j]) + int(field[i][j - 1])

print(field)
