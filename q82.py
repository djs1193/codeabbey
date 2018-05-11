#area of a polygon


def herons(x1,y1,x2,y2,x3,y3):
    a = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    b = ((x2 - x3)**2 + (y2 - y3)**2)**(1/2)
    c = ((x1 - x3)**2 + (y1 - y3)**2)**(1/2)
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return (area)



def area_polygon(xvert,yvert):

    xc = round(sum(xvert)/len(xvert))
    yc = round(sum(yvert)/len(yvert))

    individual_areas = []
    for i in range(0,len(xvert)-1):
        ar = herons(xc,yc, xvert[i],yvert[i], xvert[i+1],yvert[i+1])
        individual_areas.append(ar)
    ar = herons(xc,yc,xvert[0],yvert[0],xvert[len(xvert)-1],yvert[len(xvert)-1])
    individual_areas.append(ar)

    tot = sum(individual_areas)
    print("%.1f"%tot)


xvert = [3585 ,7160, 7508, 9580, 9470, 8027 ,7724, 3758, 2147, 1063, 273, 252 ]
yvert = [428 ,649, 940, 3131, 5454, 7504, 7811, 9478, 9105, 7656, 4336, 3647 ]

area_polygon(xvert,yvert)
