sortedarray = [180, 864, 714, 760, 967, 98, 578, 364, 667, 808, 223, 424, 923, 48, 138, 626, 477, 521, 268 ,318]
sortedarray.sort()
myarray = [180 ,864, 714, 760, 967 ,98 ,578 ,364, 667, 808, 223, 424, 923, 48, 138, 626, 477, 521, 268, 318]
posarray =[]




for i in range(0,len(myarray)):
    posarray.append(i+1)




while (myarray != sortedarray):
    for i in range(0,len(myarray)-1):
         if myarray[i] > myarray[i+1]:
                  t = myarray[i]
                  tp =str(posarray[i])
                  myarray[i]= myarray[i+1]
                  (posarray[i])= str(posarray[i+1])
                  myarray[i+1] = t
                  (posarray[i+1]) =str(tp)

s = " ".join(posarray)
print(s)
