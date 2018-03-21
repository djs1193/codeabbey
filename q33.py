#rotate string

def stringrotator(n,mystr):
    cut1 = mystr[n:]
    cut2 =mystr[0:n]
    ans = cut1+ cut2
    return ans

mylist=[
[-4, "bwsjnvffqewdxtnzbiza"],
[-4 ,"lojldiztjpfsuoxbluxpulu"],
[4 ,"invogbupmaxgubvz"],
[1 ,"luahmpoymkfssshaziejvi"],
[-1 ,"crmvdaaxbidreoiobqaty"],
[6 ,"ywxexspzeopiuqa"],
[3 ,"peyolbymvxocznyq"],
[3 ,"ajhvzqsjqqcuayup"],
[1 ,"ykggmyufpyvszyapykb"],
[-8 ,"eotedcqyqicxppweugdkz"],
[6 ,"mcinezajitolvidghgexv"]]

for i in range(0,len(mylist)):
    fin = stringrotator(mylist[i][0],mylist[i][1])
    print (fin)
    print(" ")
