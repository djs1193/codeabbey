p = [2, 4, 6, 8, 10, 12]
d = [1,2,3,4,5]

def combination(n,r):
    ans = int(fact(n)/(fact(r)*fact(n-r)))
    return(ans)

def fact(num):
    if num == 0 :
        return (1)
    else:
        tot = num
        while num > 1:
            tot = tot*(num-1)
            num -= 1
        return(tot)

def bestcomb(s,n,x):
    lim = int((s-n)/x)
    tot = 0
    for k in range(0,lim+1):
        cur = (-1)**k * combination(n,k) * combination(s-x*k-1,n-1)
        tot += cur
    return(tot)


def dungeondragons(valuestr):
    valuelist = valuestr.split()
    valuelist.pop()
    intlist = []
    for i in valuelist:
        intlist.append(int(i))

    all_dice = []
    all_side = []
    all_chance =[]
    unique_no_list = set(intlist)
    avg = round(sum(intlist)/len(intlist))
    minval = min(unique_no_list )
    maxval = max(unique_no_list )
    print(minval,maxval)
    for dices in d:
        for sides in p:
            prob = bestcomb(avg,dices,sides)
            totalrolls = sides**dices
            chances = prob/totalrolls
            all_dice.append(dices)
            all_side.append(sides)
            all_chance.append(chances)

    for i in range(0,len(all_dice)):
        if all_chance[i] > 0.01 and all_dice[i]*all_side[i] >= maxval and all_dice[i] <= minval:
            print("%dd%d %f"%(all_dice[i],all_side[i],all_chance[i]))


mystrlist = [
'19 20 22 21 17 10 22 24 25 31 28 15 23 15 31 6 23 20 18 32 11 9 26 31 18 32 25 11 23 15 24 21 31 25 18 24 20 18 14 16 24 21 30 16 27 16 18 19 19 27 19 36 33 27 31 20 22 31 21 20 29 27 23 32 17 14 28 25 25 26 26 26 20 24 19 23 17 36 25 17 14 30 21 21 21 16 29 27 16 24 24 19 26 30 13 19 21 28 14 15 0',
'4 1 1 1 6 1 3 1 3 2 2 6 5 3 3 4 5 4 4 3 2 2 5 3 2 6 6 3 4 1 5 1 1 5 2 1 5 4 1 2 6 2 2 4 5 4 1 4 1 4 1 3 6 5 6 2 4 5 4 1 6 3 2 1 1 3 1 6 1 2 2 6 3 3 4 2 6 4 5 1 2 6 4 1 4 3 3 2 2 6 3 1 2 4 1 3 1 2 3 2 0',
'9 7 2 10 6 12 9 2 8 9 6 9 13 8 16 8 14 14 8 14 9 9 12 6 11 5 13 10 9 9 7 7 6 2 10 2 8 12 9 5 5 12 5 10 13 4 9 6 4 11 13 8 5 6 10 16 11 15 8 11 16 8 14 13 2 7 10 10 7 9 9 5 4 16 8 6 6 5 9 3 9 8 6 14 7 11 15 14 8 11 5 12 4 11 3 6 7 13 13 6 0'
     ]
for i in mystrlist:
    dungeondragons(i)
    print(" ")
