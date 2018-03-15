

mylist = [
[16, 6, 72],
[12 ,18, 92],
[28 ,9, 94],
[14 ,1 ,19],
[9 ,1, 39],
[12, 4, 93],
[8 ,7, 49],
[18, 6, 15],
[15, 13, 37]]

def sum_ap(list1):
    n = list1[2]
    a = list1[0]
    d = list1[1]
    tot = int((n/2)*(2*a + (n-1)*d))
    print (tot)
    print(" ")

for i in range (0,len(mylist)):
    var_list = (mylist[i])
    sum_ap(var_list)
