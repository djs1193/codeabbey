import math

def clock(mystr):
    hour = int(mystr[:2])
    minute = int(mystr[3:])

    theta_h = math.radians(30*hour - 90 + 6*(minute/12) )
    theta_m = math.radians(6*minute)
    rh = 6
    rm = 9

    mx =math.cos(-theta_h)*rh
    print(mx +10)
    print(" ")
    my =math.sin(-theta_h)*rh
    print(my +10)
    print(" ")


    hx =math.sin(theta_m)*rm
    print(hx +10)
    print(" ")
    hy =math.cos(theta_m)*rm
    print(hy +10)
    print(" ")

list1 = [
'20:04',
'05:34',
'01:31',
'19:39',
'21:55',
'16:31'
]

for i in list1:
    clock(i)
