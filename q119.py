
graph_nodes = {}
input_list = [
['Cowsome' , 'Pikpak'],
['Mausse' , 'Mikliday'],
['Carnival' , 'Pikpak'],
['Honepy' ,'Cowsome'],
['Troffle' , 'Carnival'],
['Carnival' , 'Bawnty'],
['Pikpak' , 'Mausse'],
['Mocca' , 'Carnival'],
['Cowsome' , 'Mausse'],
['Strobry' , 'Honepy'],
['Mikliday' , 'Cowsome'],
['Mausse' , 'Mocca'],
['Bawnty' , 'Mikliday']
]
for i in range(0,len(input_list)):
    graph_nodes.update({input_list[i][0]:[]})
    graph_nodes.update({input_list[i][1]:[]})


for i in range(0,len(input_list)):
    graph_nodes[input_list[i][0]].append(input_list[i][1])
    graph_nodes[input_list[i][1]].append(input_list[i][0])


def search(initial_state,final_state):
    explored = []
    frontier = []
    in_s = initial_state
    steps = 1
    if (initial_state == final_state):
        return(initial_state)
    for i in graph_nodes[in_s]:
        frontier.append(i)
    explored.append(in_s)
    if final_state in frontier:
        return (explored[-1])
    else:
        for val in frontier:
            if val not in explored:
                for i in graph_nodes[val]:
                    frontier.append(i)
            explored.append(val)
            if final_state in frontier:
                return (explored[-1])
        return(10000)


output_list = [
['Bawnty' , 'Troffle'],
['Troffle' , 'Mausse'],
['Carnival' , 'Mikliday'],
['Carnival', 'Strobry'],
['Strobry' ,'Pikpak'],
['Troffle' , 'Pikpak'],
['Bawnty' ,'Mausse'],
['Mausse' , 'Carnival'],
['Honepy' , 'Pikpak'],
['Strobry' , 'Troffle'],
['Mausse' ,'Strobry'],
['Mocca' , 'Troffle']
]

for i in range (len(output_list)):
    dest = output_list[i][1]
    k = 0
    while dest != output_list[i][0] or dest == 10000 :
        dest = (search(output_list[i][0],dest))
        if dest == 10000:
            k = 10000
            break
        k +=1

    print(k)
    print(" ")
