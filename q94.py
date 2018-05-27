#point to segmant distance
# y = mx + c     m = (y2-y1)/(x2-x1)
def segmant_distance(data):

    if data[0] > data[2]:
        tempx = data[0]
        data[0] = data[2]
        data[2] = tempx
        tempy = data[1]
        data[1] = data[3]
        data[3] = tempy


    x1 = data[0]
    y1 = data[1]
    x2 = data[2]
    y2 = data[3]
    xp = data[4]
    yp = data[5]

    if y2 != y1 and x2 != x1:
        ms = (y2-y1)/(x2-x1)    #slope of the line segmant and line cotaining line segmant
        mp = (-1)/ms            #perpendicular lines have product of slope -1
        cs = y2 - ms*x2
        cp = yp - mp*xp


        x = (cp - cs)/(ms - mp)
        y = (ms*cp - mp*cs)/(ms-mp)

    elif y1 == y2:
        x = xp
        y = y1
    elif x1 == x2:
        y = yp
        x = x1





    if x <= x2 and x >= x1:
        d = ((xp - x)**2 + (yp - y)**2)**(1/2)
        print(d)
        print(" ")
    else:
         d1 = (((x1 - xp)**2 + (y1 - yp)**2)**(1/2))
         d2 = (((x2 - xp)**2 + (y2 - yp)**2)**(1/2))
         print(min(d1,d2))
         print(" ")


mylist = [
[12 ,7 ,16, 4, 13 ,9],
[20 ,19 ,12 ,15, 14, 10],
[1, 15, 9, 15, 6, 10],
[18 ,1 ,6 ,10, 5, 20],
[5, 4, 16, 15, 4, 8],
[4 ,4 ,17, 20, 12, 9],
[10, 8, 8, 1, 9, 10],
[12, 5, 10, 0, 3, 15],
[0 ,18, 17, 6, 0, 16],
[15, 12, 6, 11, 7, 1],
[0, 12, 2, 17, 7, 19],
[6, 1, 20, 15, 12, 11],
[10, 14, 8, 20, 2, 3],
[15, 15, 5, 12, 15, 8],
[13, 17, 4, 20, 1, 13],
[18, 8, 3, 0, 8, 12],
[12, 11, 17, 12, 4, 16],
[15, 15, 14, 2, 5, 20],
[11, 10, 3, 16, 15, 8]
]

for i in mylist:
    segmant_distance(i)
