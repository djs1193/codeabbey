#Binary search to solve math eq

import math


def solve(a, b, c, d, first, last):
    x = (float(first) + float(last)) / 2
    ans = round((a * x + b * math.sqrt(x**3) - c * math.exp(-x / 50) - d), 7)

    if ans > 0:
        res = ( solve(a, b, c, d, first, x))
    elif ans < 0:
        res =( solve(a, b, c, d, x, last))
    else:
        res = ( str(x))
    return (res)

list1=[
[0.59912051, 0.64030348, 263.33721367, 387.92069617],
[15.68387514 ,1.26222280, 695.23706506, 698.72384731]
]
for i in list1:
    A = i[0]
    B = i[1]
    C = i[2]
    D = i[3]
    ans = solve(A, B, C, D, 0, 100)
    print(ans)
