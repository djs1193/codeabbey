def lcg(a,c,m,x,n):
    for i in range(0,n):
        xnext = (a*x +c)%m
        x = xnext
    print(x)
    print(" ")
mylist = [
[923 ,7 ,45, 8, 4],
[65 ,34378, 96, 42, 3],
[309, 88850, 4 ,1, 5],
[53, 30 ,8075, 7687, 10],
[29 ,5 ,217, 115 ,24],
[75 ,70, 72, 52, 3],
[1007, 23818, 233174, 28680, 23],
[107 ,14686, 89, 30, 15],
[737, 5, 5590, 1894, 3],
[1221 ,11571, 46, 6, 7],
[117, 85, 33, 24, 19],
[1363, 8484 ,551 ,348, 14],
[139, 995763, 24, 0, 4],
[1529, 17, 33, 11, 7],
[117, 7, 775505, 278167, 18],
[33, 1066, 4, 1, 15],
[91 ,2520, 5720, 1873, 13]
]
for k in mylist:
     lcg(k[0],k[1],k[2],k[3],k[4])
