#bubblesorting

slist = [11 ,15, 4, 8, 12, 16, 10, 17, 14, 6 ,7 ,2, 3, 5, 1, 9, 13]
slist.sort()
alist = [11 ,15, 4, 8, 12, 16, 10, 17, 14, 6, 7, 2, 3, 5, 1, 9, 13]



swap_c  = 0
pass_c = 0

while (alist != slist):
    for i in range(0,len(alist)-1):
         if alist[i] > alist[i+1]:
                  t = alist[i]
                  alist[i]= alist[i+1]
                  alist[i+1] = t
                  swap_c = swap_c +1
    pass_c = pass_c + 1

print(pass_c +1)
print(" ")
print(swap_c)
