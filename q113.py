
def total_gems(N,T):
    my_input = [N,T]
    last_val = my_input[0]
    jumps = my_input[1]
    loop_list = []
    for rep in range(0,jumps):
        for i in range(0,last_val):
            loop_list.append(i)
    loop_list.append(0)
    line_segs = {}
    for i in range(0,last_val):
        line_segs.update({i:0})



    segment_crossed = 0
    index = 0
    while index <= len(loop_list) -jumps:
        line_segs[loop_list[index]] +=1
        line_segs[loop_list[index+jumps]] +=1
        if loop_list[index] < loop_list[index+jumps]:
            for i in range(loop_list[index+1],loop_list[index+jumps]):
                segment_crossed += line_segs[i]
            index += jumps

        else:
            for i in range(0,loop_list[index+jumps]):
                segment_crossed += line_segs[i]
            for i in range(last_val-1,loop_list[index],-1):
                segment_crossed += line_segs[i]
            index += jumps
    print(segment_crossed)
    print(" ")



input_list = [
[17 ,5],
[17 ,2],
[9 ,2],
[16 ,3],
[11 ,5],
[15 ,4],
[14 ,5]
]
for i in input_list:
    total_gems(i[0],i[1])
