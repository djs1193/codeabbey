#200 500

# 4p +2g = 200
# xp +2g = 500
# xp - 4p = 300
# p(x-4) = 300
# p = (300/x-4)   x>4 and x is even

def pigsandgirls(legs,breasts):
    possible = 1
    val = breasts-legs
    for x in range(6,val+1,2):
        p = (val/(x-4))
        if p.is_integer() and 4*p < legs :
            possible +=1
    print(possible)

mylist = [
[1824, 10608],
[1156, 4418],
[400 ,1088],
[1664, 8036],
[1076, 5780],
[310, 586],
[96 ,580],
[372, 870],
[104, 610],
[5172, 16772],
[154, 698],
[40, 64],
[114, 634],
[4852, 31516]
]
for i in mylist:
    pigsandgirls(i[0],i[1])
    print(" ")
