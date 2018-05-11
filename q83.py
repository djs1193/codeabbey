#cloud height measurement
# H   =   tan(B) * D2
# H   =   tan(A) * (D1 + D2)   =   tan(A) * D1  +  tan(A) * D2
# H   =   tan(A) * (D1 + D2)   =   tan(A) * D1  +  tan(A) *
# H = D1.tan(A).tan(B)/(tan(A)-tan(B))


import math

def cloud_height(d,theta_a,theta_b):

    radian_a = math.radians(theta_a)
    radian_b= math.radians(theta_b)

    h = d*math.tan(radian_a)*math.tan(radian_b)/(math.tan(radian_b) - math.tan(radian_a))
    print(round(h))



list_d = [1449,631,828,1826,2224,809,1917,1822,1215,2718,628,1578,682,2136,1834,2912]
list_a = [25.6742, 34.5923, 39.5740, 25.4617, 32.0071, 39.3463, 24.7379, 28.5221, 25.6785, 23.9625, 36.5199, 31.5253, 39.1013, 27.7573, 28.7866, 22.8790]
list_b = [59.4804, 55.7652, 56.1722, 56.5714, 66.2625 ,63.4349, 53.1165, 56.1827, 61.6343, 60.7642, 66.7507, 62.9652, 63.0005, 51.3330, 62.9784, 62.5393]

for i in range(0,len(list_a)):
    cloud_height(list_d[i],list_a[i],list_b[i])
    print(" ")
