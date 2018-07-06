##################### djikstra algo ######################################

all_y = []
def lcg(a,c,m,x,n):
    for i in range(0,n):
        xnext = (a*x +c)%m
        all_y.append(xnext % 951 +1)
        x = xnext

lcg(445 ,700001 ,2097152,577,951*4)
vertix =  {}
weights = {}

for i in range(1,952):
    vertix.update({i:[]})
for i in range(1,952):
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

for i in range(1,952):
    reverse_vertix.update({i:[]})
for i in range(1,952):
    reverse_weights.update({i:[]})

for i in vertix:
    for k in range(1,952):
        if int(i) in vertix[k] and int(k) not in vertix[i]:
            index = vertix[k].index(int(i))
            reverse_vertix[i].append(int(k))
            reverse_weights[i].append(weights[k][index])
for i in vertix:
    if i in reverse_vertix:
        for val in reverse_vertix[i]:
            vertix[i].append(val)
for i in weights:
    if i in reverse_weights:
        for val in reverse_weights[i]:
            weights[i].append(val)

################################################################################


def djikstra(curr_node,dest):
    tentative_weights = {}
    visited_set = []
    unvisited_set = [i for i in range(1,952)]
    cond  = True
    for i in range(1,952):
        if i == 252:
            tentative_weights.update({i:0})
        else:
            tentative_weights.update({i:10000000})
    tot_weight = 0
    while cond :
        possible_nodes = []
        tot_weight = tentative_weights[curr_node]
        if curr_node not in visited_set:
            for node in vertix[curr_node]:
                    if node not in visited_set:
                        new_weight = weights[curr_node][vertix[curr_node].index(node)] + tot_weight
                        if new_weight < tentative_weights[node] :
                            tentative_weights[node] = new_weight
            visited_set.append(curr_node)
            unvisited_set.pop(unvisited_set.index(curr_node))

        if dest in visited_set :
            cond  = False
        else:
            for i in unvisited_set:
                possible_nodes.append(tentative_weights[i])
            val = min(possible_nodes)
            for n in tentative_weights :
                if tentative_weights[n] == val and n not in visited_set:
                    curr_node    =  n
    print(tot_weight)
    print(" ")

for i in range(1,952):
    djikstra(252,i)
