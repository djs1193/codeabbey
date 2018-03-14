mylist1 =[
[216 ,248, 192],
[144, 74, 193],
[329, 218, 174],
[247 ,261, 60],
[223, 216, 85],
[139, 1 ,1],
[260, 19, 5],
[29 ,58, 103],
[88, 14, 43],
[302, 223, 4],
[22, 83, 169]]


def myfunc1(a,b,c):
    res = ((a*b) + c)
    return res

def myfunc2(n):
    tot =0
    while(n>=1):
         r = n%10
         d = int(n/10)
         tot = tot + r
         n = d
    return tot


for q in range(0,len(mylist1)):
        x = myfunc1(mylist1[q][0],mylist1[q][1],mylist1[q][2])
        y = myfunc2(x)
        print(y)
        print(" ")
