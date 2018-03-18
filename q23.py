list1 =[
[18, 23, 59, 59, 23, 9, 41, 1],
[4 ,5 ,55, 29, 20, 2, 23, 47],
[1 ,16, 28, 19, 20, 5 ,34, 28],
[2 ,14, 11, 39 ,4 ,14, 12, 19],
[18, 2 ,51, 34, 25, 17, 53, 21],
[2 ,16, 36, 13, 24, 8 ,59, 55],
[17, 11, 35, 35, 22, 10, 47, 58],
[26, 6, 13, 46, 28, 2 ,24, 56],
[0 ,8 ,31, 14, 8, 7, 12, 44],
[4, 10, 0, 49, 15, 15, 2, 55],
[10, 3, 51, 26, 16, 4 ,16, 30],
[8, 9, 19, 57, 29, 22, 50, 41]]

list2 =[8 ,4, 6, 47, 9, 11, 51, 13]

emptylist = []

def timediff(mylist):
    s = str((mylist[7] - mylist[3])%60)
    if (mylist[7] < mylist[3]):
        mylist[6] = mylist[6]-1
    m = str((mylist[6] - mylist[2])%60)
    if (mylist[6] < mylist[2]):
        mylist[5] = mylist[5]-1
    h =str((mylist[5] - mylist[1])%24)
    if (mylist[5] < mylist[1]):
        mylist[4] = mylist[4]-1
    d =str((mylist[4] - mylist[0]))
    emptylist = [d,h,m,s]
    mystr = " ".join(emptylist)
    print ("(%s)" %mystr)
for i in range(0,len(list1)):
    timediff(list1[i])
