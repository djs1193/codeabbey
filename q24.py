mystring = """
+ 1
* 2
+ 3146
* 4
+ 6
+ 1887
* 1308
+ 1
+ 89
* 277
* 5
* 8737
+ 6335
* 753
+ 10
+ 745
+ 59
+ 6180
+ 10
* 58
+ 5795
* 4
* 235
+ 87
+ 89
* 5185
* 8562
+ 664
+ 275
* 75
+ 521
* 7
* 220
* 479
* 832
+ 80
+ 5594
* 2541
+ 892
* 4
+ 94
* 9
+ 691
* 4
* 92
+ 190
* 95
+ 7787
% 4503"""


def modularcalculator(n,mystr):
    mylist = mystr.split()
    for i in range(0,len(mylist),2):
        if mylist[i] == "+":
            n = n + int(mylist[i+1])
        elif mylist[i] == "*":
            n = n * (int(mylist[i+1]))
        elif mylist[i] == "%":
            n = n % (int(mylist[i+1]))
    print(n)



modularcalculator(45,mystring)
