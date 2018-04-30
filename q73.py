import math

def treeheight(d,a):
    theta = a - 90
    radian = math.radians(theta)
    h = d*math.tan(radian)
    print(round(h))

list1 = [
[98 ,123.959],
[142, 109.038],
[60 ,104.931],
[59, 131.934],
[74 ,132.158],
[76 ,118.926],
[48 ,136.736],
[71 ,104.982],
[49 ,129.920],
[25, 120.964],
[127, 113.035],
[92, 108.060],
[81, 117.962]
]

for i in list1:
    treeheight(i[0],i[1])
    print(" ")
