#brainfuck interpreter
mystr = """;>;<[->+>++<<]>++++<[->+>++<<]+++>:<[->+>++<<]>:<[->+>++<<][>+<-]>-<:>++++<>;<>:<+:>-:<[>+<-]>:<+:>-:<[->+>++<<][->+<][->++<]>;<;>-<:[->+>+<<]>>[-<<+>>]<<+++;>:<[>+<-];>:<>:<:>:"""

mylist = []
for i in mystr:
    mylist.append(i)


inputlist = [13, 15, 18, 17, 4, 5, 2 ]
mainlist = []
for i in range(0,len(inputlist)):
    mainlist.append(0)                #creating empty cells assuming cells <= number of inputs

c = 0
i = 0
pos = 0
skip = 0


while i < len(mylist):
    if mylist[i] == ";":
        mainlist[c] = inputlist[pos]
        pos += 1
        i += 1
    elif mylist[i] == ">":
        c += 1
        i += 1
    elif mylist[i] == "<":
        c -=1
        i += 1
    elif mylist[i] == ":":
        print(mainlist[c])
        print(" ")
        i += 1
    elif mylist[i] == "-":
        mainlist[c] -=1
        i += 1
    elif mylist[i] == "+":
        mainlist[c] +=1
        i += 1
    elif mylist[i] == "[" and mainlist[c] !=0:
        val = i
        i += 1
    elif mylist[i] == "[" and mainlist[c] ==0:
        skip = i
        while mylist[skip] != "]":
            skip += 1
        i = skip+1
        skip = 0
    elif mylist[i] == "]" and mainlist[c] !=0 :
        i = val
    elif mylist[i] == "]" and mainlist[c] == 0:
        i+=1
