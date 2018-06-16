#BINARY HEAP

inputs = "36 28 0 17 2 0 18 0 23 27 0 8 24 0 12 13 0 38 0 14 0 21 0 30 0 32 22 3 1 0 7 0 29 34 16 25 9 40 6 4 31 5 37 11 10 0 33 20 19 35 39 0 15 26 0".split()
mylist = []
for i in inputs:
    mylist.append(int(i))

heap = []


for i in mylist:
    if i != 0:
        heap.append(i)
        element_pos = len(heap) - 1
        while element_pos > 0:
            if heap[element_pos] < heap[int((element_pos-1)/2)]:
                temp = heap[element_pos]
                heap[element_pos] = heap[int((element_pos-1)/2)]
                heap[int((element_pos-1)/2)] = temp
                element_pos = int((element_pos-1)/2)
            else:
                element_pos = 0
    else:
        heap[0] = heap[-1]
        heap.pop()
        element_pos = 0
        while element_pos < (len(heap))/2 -1:
            val = min(heap[2*element_pos+1],heap[2*element_pos+2])
            if heap[element_pos] > heap[2*element_pos+1] and val == heap[2*element_pos+1] :
                temp = heap[element_pos]
                heap[element_pos] = heap[2*element_pos+1]
                heap[2*element_pos+1] = temp
                element_pos = 2*element_pos+1
            elif heap[element_pos] > heap[2*element_pos+2] and val == heap[2*element_pos+2] :
                temp = heap[element_pos]
                heap[element_pos] = heap[2*element_pos+2]
                heap[2*element_pos+2] = temp
                element_pos = 2*element_pos+2
            else: element_pos = (len(heap))/2

for i in heap:
    print(i)
    print(" ")
