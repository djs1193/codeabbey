def quicksort(array, left, right):
    print("%d-%d "%(left,right))
    pivot_pos = partition(array, left, right)
    if pivot_pos - left > 1:
        quicksort(array, left, pivot_pos - 1)
    if right - pivot_pos > 1:
        quicksort(array, pivot_pos + 1, right)


def partition(array, left, right):
    lt = left
    rt = right
    di = 'left'        #specifies at which side is currently "empty" space
    pivot = array[left]
    temp = pivot
    while lt < rt:
        if di == 'left':
            if array[rt] > pivot:
                rt = rt - 1
            else:
                array[lt] = array[rt]
                array[rt] = temp
                lt = lt + 1
                di =  'right'
        else:
            if array[lt] < pivot:
                lt = lt + 1

            else:
                array[rt] = array[lt]
                array[lt] = temp
                rt = rt - 1
                di = 'left'#here lt = rt - both points to empty cell where pivot should return
    return lt




stralist = """
158 41 53 106 149 115 101 35 165 185 192 73 83 52 190 79 116 136 122 129 49 124
 91 127 167 3 97 183 11 171 69 132 139 25 153 160 186 57 154 163 65 22 99 85 13
 1 199 168 82 197 175 135 113 100 28 20 144 176 172 130 31 143 166 27 24 68 18
89 141 196 90 9 123 112 51 157 94 156 14 33 29 133 169 145 119 155 178 173 164
74 39 61 54 182 23 70 66 71 46 120 170 108 195 92 63 109 15 118 8 128 43 47 87
162 86 5 55 26 93 34 104 181 189"""
strlist = stralist.split()
Array = []
for i in strlist:
    Array.append(int(i))
low = 0
up = len(Array)-1
quicksort(Array,low,up)
