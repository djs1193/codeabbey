#graph generator

all_y = []
def lcg(a,c,m,x,n):
    for i in range(0,n):
        xnext = (a*x +c)%m
        all_y.append(xnext % 11 +1)
        x = xnext

lcg(445 ,700001 ,2097152,1291,44)
print(all_y)

vertix =  {}
weights = {}

for i in range(1,12):
    vertix.update({i:[]})
for i in range(1,12):
    weights.update({i:[]})

i = 1
for k in range(0,len(all_y),4):
    if  i != all_y[k] and all_y[k] not in vertix[i] and i not in vertix[all_y[k]] :
        vertix[i].append(all_y[k])
        weights[i].append(all_y[k+1])
    if  i != all_y[k+2] and all_y[k+2] not in vertix[i] and i not in vertix[all_y[k+2]]:
        vertix[i].append(all_y[k+2])
        weights[i].append(all_y[k+3])
    i+=1

reverse_vertix = {}
reverse_weights = {}

for i in range(1,12):
    reverse_vertix.update({i:[]})
for i in range(1,12):
    reverse_weights.update({i:[]})

for i in vertix:
    for k in range(1,12):
        if int(i) in vertix[k] and int(k) not in vertix[i]:
            index = vertix[k].index(int(i))
            reverse_vertix[i].append(int(k))
            reverse_weights[i].append(weights[k][index])

print(vertix)
print(weights)
print(reverse_vertix)
print(reverse_weights)

for i in range(1,12):
    print( sum(weights[i])+ sum(reverse_weights[i]))
    print(" ")
