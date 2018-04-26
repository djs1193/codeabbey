
def InsertionSort(mystr):
    mylist1 = mystr.split()
    mylist = []
    for k in mylist1:
        mylist.append(int(k))
    for i in range(1,len(mylist)):
        count = 0
        t = mylist[i]
        for v in range(i,0,-1):
            if t < mylist[v-1]:
                mylist[v] = mylist[v-1]
                mylist[v-1] = t
                count += 1
        print(count)



mystr = """149 55 92 93 106 60 51 189 4 112 22 133 24 49 2 46 199 102 87 156
 84 52 135 32 74 7 161 155 17 113 122 173 99 111 176 12 109 35 181 110 28 125
 115 67 10 166 88 144 197 19 40 159 177 152 8 11 118 143 33 186 56 31 147 114
 193 124 1 192 107 34 95 25 154 54 120 158 167 153 145 183 131 98 18 79 13 27
 72 119 61 38 121 139 100 76 63 123 194 21 69 73 80 103 164 3 78 142 85 198
116 127 36 128 160 5"""
InsertionSort(mystr)
