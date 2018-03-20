#bubblesorting

alist = [8655 ,659, 97, 6, 6125, 77, 6989, 484, 84, 29, 5, 3, 7661, 3460, 15587, 6539, 6, 2672, 733,
         46384 ,2651, 57, 69805, 4, 4953, 889, 59636, 62, 87, 26895, 7, 4188, 58, 86, 18, 11, 556, -1]
mv = max(alist)
l = len(alist)-2

swap_c  = 0

for i in range(0,len(alist)-2):
         if (alist[l]== mv):
             break
         elif alist[i] > alist[i+1]:
                  t = alist[i]
                  alist[i]= alist[i+1]
                  alist[i+1] = t
                  swap_c = swap_c +1

print(swap_c)


def checksum(list1):
    res = 0
    for i in range(0,len(list1)-1) :
        res = res + list1[i]
        res = (res*113)%10000007
    print(res)


checksum(alist)
