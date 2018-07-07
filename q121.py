#implementation of DFS

N = 40
graph_nodes = {}
for i in range(0,N):
    graph_nodes.update({i:[]})

input_list = [

[19 ,35],
[27 ,38],
[4 ,30],
[33 ,2],
[34 ,24],
[35 ,34],
[0 ,4],
[24 ,14],
[21 ,31],
[38 ,20],
[0 ,24],
[21 ,37],
[15 ,35],
[6 ,25],
[21, 7],
[2 ,0],
[31 ,10],
[9 ,33],
[15 ,28],
[36 ,10],
[11 ,2],
[37 ,12],
[20 ,32],
[12 ,25],
[7 ,24],
[31 ,32],
[0 ,38],
[39 ,19],
[10 ,18],
[1 ,35],
[1 ,14],
[19 ,34],
[9 ,32],
[30 ,37],
[16 ,30],
[19 ,37],
[4 ,27],
[3 ,5],
[23 ,8],
[14 ,17],
[23 ,18],
[36 ,12],
[37 ,14],
[15 ,22],
[1 ,32],
[6 ,11],
[29 ,17],
[29 ,13],
[7 ,25],
[21 ,16],
[37 ,6],
[19 ,5],
[6 ,38],
[38 ,17],
[21 ,38],
[14 ,21],
[33 ,29],
[13 ,20],
[28 ,29],
[9 ,28],
[27 ,31],
[28 ,39],
[26 ,4],
[38 ,36],
[11 ,39],
[35 ,39],
[18 ,22],
[9 ,16],
[23 ,10],
[36 ,5],
[18 ,39],
[22 ,6],
[23 ,7],
[6 ,17],
[19 ,18],
[18 ,14],
[37, 18],
[30 ,8],
[20 ,26],
[5 ,38],
[39 ,10],
[23 ,13],
[34 ,31],
[9 ,25],
[11 ,5],
[29 ,21],
[31 ,14],
[33 ,27],
[32 ,0],
[15 ,3],
[26 ,8],
[32 ,28],
[32 ,12],
[0 ,23],
[6 ,15],
[5 ,30],
[14 ,32]
]
for val in input_list:
    graph_nodes[val[0]].append(val[1])
    graph_nodes[val[1]].append(val[0])

for ls in graph_nodes:
    graph_nodes[ls].sort()




curr_node = 0
frontier = []
explored = []
frontier.append(curr_node)
while len(frontier) != 0:
        curr_node = frontier.pop()
        if curr_node in explored:
            continue
        else:
            explored.append(curr_node)
            for i in reversed(graph_nodes[curr_node]):
                if i not in explored:
                    frontier.append(i)


def dfs(node):
    index_node = explored.index(node)
    ex = explored[:index_node]
    for val in reversed(ex):
        if node in graph_nodes[val]:
            return(val)



points = [-1]
for i in range(1,N):
    ans = (dfs(i))
    points.append(ans)

for k in points:
    print(k)
    print(" ")
