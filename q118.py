N = 44
graph_nodes = {}
for i in range(0,N):
    graph_nodes.update({i:[]})

input_list = [
[4 ,20],
[23 ,13],
[6 ,26],
[29 ,33],
[39 ,28],
[7 ,27],
[5 ,26],
[37 ,20],
[13 ,3],
[38 ,2],
[9 ,39],
[31 ,34],
[24 ,15],
[28 ,38],
[34 ,9],
[10 ,18],
[27 ,34],
[35 ,11],
[22 ,31],
[19 ,32],
[9 ,32],
[30 ,29],
[13 ,37],
[17 ,9],
[39 ,26],
[16 ,14],
[2 ,1],
[3 ,38],
[26 ,29],
[30 ,9],
[4 ,23],
[22 ,0],
[7 ,8],
[1 ,3],
[33 ,1],
[2 ,20],
[7 ,2],
[10 ,2],
[9 ,42],
[9 ,43],
[29 ,39],
[3 ,12],
[15 ,13],
[11 ,19],
[13 ,42],
[11 ,3],
[43 ,26],
[28 ,32],
[32 ,0],
[21 ,0],
[40 ,29],
[42 ,19],
[4 ,0],
[22 ,14],
[13 ,2],
[25 ,8],
[9 ,27],
[31 ,19],
[42 ,41],
[41 ,38],
[41 ,30],
[14 ,27],
[33 ,10],
[26 ,12],
[34 ,17],
[21 ,43],
[4 ,26],
[34 ,38],
[38 ,23],
[16 ,21],
[12 ,39],
[23 ,5],
[24 ,11],
[41 ,18],
[38 ,17],
[36 ,43],
[31 ,41],
[24 ,34],
[1 ,7],
[36 ,8],
[12 ,0],
[9 ,40],
[2 ,22],
[37 ,5],
[4 ,24],
[18 ,7],
[38 ,32],
[17 ,21],
[28 ,26],
[33 ,6],
[2 ,37],
[1 ,30],
[25 ,39],
[22 ,32],
[25 ,11],
[7 ,40],
[17 ,33],
[16 ,40],
[12 ,16],
[33 ,15],
[30 ,19],
[19 ,6],
[5 ,10],
[22 ,20],
[2 ,6],
[17 ,7],
[41 ,25],
[43 ,27],
[35 ,18],
[31 ,10],
[9 ,7],
[35 ,16],
[6, 17],
[21 ,40],
[33 ,11],
[24 ,10],
]
for val in input_list:
    graph_nodes[val[0]].append(val[1])
    graph_nodes[val[1]].append(val[0])

for ls in graph_nodes:
    graph_nodes[ls].sort()


def search(node):
    explored = []
    frontier = []
    path= 0
    for i in graph_nodes[path]:
        frontier.append(i)
    explored.append(path)
    if node in frontier:
        return (explored[-1])
    else:
        for val in frontier:
            if val not in explored:
                for i in graph_nodes[val]:
                    frontier.append(i)
            explored.append(val)
            if node in frontier:
                return (explored[-1])

points = [-1]
for i in range(1,N):
    ans = (search(i))
    points.append(ans)

for k in points:
    print(k)
    print(" ")
