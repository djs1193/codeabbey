myinput = """ 55 50 101 15 148 94 95 2 42 23 83 30 154 122 169
 107 16 147 158 87 155 51 189 43 26 175 97 41 93 145 96 142 47
  110 91 140 5 182 27 176 13 180 99 181 88 193 196 36 151 190 73
   34 28 48 131 69 141 76 164 123 74 174 64 78 67 46 105 44 59 85
   40 173 135 37 9 86 120 199 116 184 65 163 6 150 92 170 8 113 127
   72 121 117 162 70 144 10 49 100 172 178 103 197 132 24 82 137 77
   138 130 53 156 108 29 12 98 152 167 112 52 106 63 79 146 177 124 129"""


list1 = myinput.split()
mylist = []
for i in list1:
    mylist.append(int(i))
last =len(mylist)



while last > 1:
    pos = 0
    temp = max(mylist)
    for i in range(0,last):
        if mylist[i] == temp:
            pos = i
            print(i)
            print(" ")
    mylist[pos] = mylist[last-1]
    mylist[last-1]=temp
    mylist.pop()
    last -=1
