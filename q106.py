import math

A = -0.7
B = -0.3
C = 5
dt = 10**(-9)

myinput = [
-1 ,-0.4,
0.2 ,0.9,
0.6 ,-0.3,
-0.8 ,0.9,
0.4 ,-0.3,
-0.3 ,0.6,
-0.6 ,0.5,
-0.4 ,-0.7,
0.9 ,0.4,
-1 ,0.6,
1 ,-0.4,
-0.4 ,0.1,
0.8 ,1,
-0.3 ,0.9
]

allx = []
ally = []

for i in range(0,len(myinput)):
    if i%2 == 0:
        allx.append(myinput[i])
    else:
        ally.append(myinput[i])

for i in range(0,len(allx)):
    x = allx[i]
    y = ally[i]
    f = (x - A)**2 + (y - B)**2 + (C*(math.exp((- (x + A)**2 - (y + B)**2))))
    varx =  (x + dt - A)**2 + (y - B)**2 + C * math.exp((- (x + dt + A)**2 - (y + B)**2))
    vary =  (x - A)**2 + (y + dt - B)**2 + C * math.exp((- (x + A)**2 - (y + dt + B)**2))
    valx = (varx - f)/dt
    valy = (vary - f)/dt
    theta = math.atan2(valy,valx)
    print(round(math.degrees(theta)) + 180)
    print(" ")
