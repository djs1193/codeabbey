#neumanns random generator

mylist = ['7735', '2754', '3453', '746', '3234', '4421' ,'3017' ,'2663', '9348', '6694']

def neumanns(mystr):
     n = int(mystr)
     first = n**2
     pad = "%08d"%(first)
     newstr = str(pad)
     nextstr = pad[2:6]
     return nextstr

for i in mylist:
    emptylist = [i]
    x = neumanns(i)
    while x not in emptylist:
       emptylist.append(x)
       x = neumanns(x)

    print(len(emptylist))
