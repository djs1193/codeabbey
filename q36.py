counter = 1
myarray  =[]
for i in range(1,37):
    myarray.append(i)


def josephus(arr,n,c=10):
    global counter
    for k in range(0,n):
        if counter%c == 0:
            arr[k]='x'
        counter = counter + 1
    return arr


def newarray(alist):
    emptylist = []
    for i in range(0,len(alist)):
        if alist[i] != 'x':
            emptylist.append(alist[i])
        else:
            continue
    return emptylist

while(len(myarray) != 1):
   x=josephus(myarray,len(myarray))
   y = newarray(x)
   myarray = y
print(y[0])
