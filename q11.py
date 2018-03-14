#sorting an array to get median value
mainlist =[[1314, 1323, 539],
[4 ,98, 77],
[159, 96, 94],
[646, 1313 ,604],
[9 ,45, 12],
[28 ,26 ,11],
[4 ,324, 11],
[165, 506 ,158],
[881, 5 ,14],
[254, 320, 226],
[12, 2, 74],
[59 ,90 ,65],
[936 ,980, 1034],
[12 ,14, 5],
[911 ,27 ,18],
[356 ,352, 436],
[891, 833 ,300],
[385, 350, 349],
[339 ,21 ,340],
[379, 105, 6],
[99 ,151, 109],
[867, 859, 829],
[967 ,1867, 966],
[1121, 411, 492],
[50 ,52, 791],
[31, 774, 772],
[151, 5, 147]]

for p in range(0,len(mainlist)):
    list1 = mainlist[p]
    list1.sort()
    print(list1[1])
    print(" ")

#how sort is working
#if A > B swap A with B
#if B > C swap B with C
#if A > B swap A with B
#use temp variable for swapping
