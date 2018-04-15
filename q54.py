def quadratic_roots(A,B,C):
    x1 = str(((-B) + ((B**2) - (4*A*C))**(1/2))/(2*A))
    x2 = str(((-B) - ((B**2) - (4*A*C))**(1/2))/(2*A))
    if x1[0] == '(':
        x1 = x1.strip('(')
        x1 = x1.strip(')')
        x2 = x2.strip(')')
        x2 = x2.strip('(')

        for var in x1:
            if var =='j':
               x1 = x1.replace(var,'i')
        for var in x2:
            if var =='j':
               x2 = x2.replace(var,'i')
        print("%s %s;"%(x1,x2))
        print(" ")
    else:
        print("%s %s;"%(x1,x2))
        print(" ")





list1 = [
[3 ,-6 ,51],
[5 ,-90, 410],
[7 ,0, 112],
[1, -18, 82],
[9 ,36, 0],
[3 ,-9 ,-210],
[1 ,10, 125],
[7 ,14 ,707],
[6 ,78, 240],
[4 ,56 ,212],
[4 ,0, 0],
[1, -4, 5],
[4 ,-12 ,8],
[6 ,-30 ,24]
]
for i in list1:
    quadratic_roots(i[0],i[1],i[2])
