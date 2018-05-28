
import sys

def maxvalue(path,pos):
    if(pos < 0):
        return 0
    elif pos == 0 :
        return path[pos]
    else:
        return path[pos] + max((maxvalue(path,pos-2)),(maxvalue(path,pos-3)))

inputs = [
[14, 18, 10, 5 ,14 ,3 ,8 ,9 ,15 ,11 ,6 ,7 ,9 ,10, 5 ,4 ,9 ,8 ,11, 17],
[3, 12, 2 ,12 ,5 ,9 ,11 ,10 ,15 ,12 ,4 ,13 ,2 ,7 ,8 ,4 ,14 ,15 ,17 ,5 ,2 ,5 ,13 ,10 ,8 ,16],
[15, 7 ,16 ,4 ,8 ,9 ,5 ,19 ,12 ,13 ,11 ,2 ,9, 3, 4, 2, 4 ,10, 9 ,6 ,5 ,5 ,4 ,9 ,5 ,7 ,2 ,13, 14, 16, 12, 10, 3, 8],
[10, 16, 17, 9 ,8 ,11, 18, 9, 18, 2, 11, 19, 4, 2, 8, 9, 5, 11, 12, 12, 14, 18, 13, 8, 13, 9, 18, 4, 11, 7],
[19, 3, 12 ,8, 10, 4, 7, 17, 2 ,8 ,9 ,19, 11, 9, 7, 18, 13, 17, 11, 6, 11, 9, 18, 18, 3, 7, 16, 5, 16, 4 ,18, 15],
[11, 4, 14, 13, 10, 11, 14, 16, 18, 13, 7, 8 ,19, 6, 2, 16, 15, 7, 7, 5, 5, 5, 6],
[2, 9, 8, 5, 8, 3, 9, 18, 6, 3, 12, 14, 13, 6 ,10, 12, 17, 15, 18, 16, 19, 19, 12, 15, 7, 18, 18, 10],
[4, 2, 5, 11, 8 ,8, 18, 10, 16, 16, 14, 17, 8 ,8 ,11, 12, 17, 3, 9, 12, 2, 6],
[2, 17, 7, 7, 16, 5, 16, 18, 8, 16, 4, 18, 4, 10, 16, 12, 7 ,13, 6 ,4 ,19, 13, 14, 12, 10, 15, 2 ,3 ,15],
[14, 16, 3 ,2 ,3, 17, 5, 17, 16, 12, 13, 19, 10, 15, 10, 7 ,8 ,15, 18, 12, 18, 17 ,6 ,12],
[14, 7 ,10 ,16, 3 ,14, 10, 17, 16 ,10, 19, 14, 14, 16, 11, 6 ,9 ,10, 15 ,5 ,18, 2, 11, 13, 19, 4 ,11],
[8 ,3 ,7 ,3 ,9, 15, 17, 11, 10, 8 ,8 ,7, 16, 8, 19, 11, 4 ,11, 15, 12, 19, 11, 16, 18, 12, 7, 11, 11, 10, 3, 9, 16, 5],
[17, 12, 10, 15, 4 ,18, 3, 11, 5 ,17, 17, 5, 8, 19, 14, 4, 11, 13, 14, 7 ,12, 6, 13, 4 ,16, 3, 5, 5 ,18, 9 ,18],
[2 ,8 ,11 ,4 ,6 ,12, 13, 10, 10, 10, 13, 17, 10, 7, 2, 2, 19, 14, 8, 12, 19, 19, 14, 16, 3, 17, 2, 19, 6, 18, 15, 6],
[7, 8, 11, 17, 2, 19, 8 ,10, 13, 5, 18, 19, 5, 18, 19, 18, 6 ,11, 18, 6, 5, 14, 7, 2],
[7, 7, 12, 3, 12, 17, 8 ,19, 9, 6, 19, 8, 12, 10, 2 ,16, 9, 19, 19, 7, 18, 18, 12, 10, 16, 17, 13, 10, 5, 14, 5],
[2, 16, 12, 12, 13, 19, 11, 2, 5, 11, 9, 16, 19, 10, 12, 8, 9, 12, 14, 8, 10, 7, 16, 6, 4, 10, 14],
[4, 18, 16, 4, 14, 8, 15, 7, 7, 7, 8, 11, 16, 16, 7 ,16, 6, 17, 5, 14, 9, 18, 2 ,17],
[17, 4, 7, 7, 17, 13, 9, 15, 9, 12, 9, 16, 7, 15, 4, 12, 3, 13, 9, 17, 19, 5, 4]
]
for array in inputs:
    path = list(reversed(array))
    pos = len(path) -1
    path1 = ((maxvalue(path,pos)))
    path.pop(0)
    path2 = ((maxvalue(path,pos-1)))
    print(max(path1,path2))
    print(" ")
