#combinations

def comb(n,k):
    totn = 1
    totk = 1
    totd = 1
    d = n-k
    for i in range(n,0,-1):
        totn = totn*i
    for i in range(k,0,-1):
        totk = totk*i
    for i in range(d,0,-1):
        totd = totd*i
    print(int(totn/(totk*totd)))
    print(" ")

list1 = [
[108, 7],
[119 ,112],
[96 ,7],
[97 ,7],
[72 ,65],
[54 ,10],
[114 ,107],
[61 ,9],
[78 ,8]
]

for i in list1:
    comb(i[0],i[1])
