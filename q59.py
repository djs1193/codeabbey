# Python program to print prime factors

import math

# A function to print all prime factors of
# a given number n
def primeFactors(n):
    mylist = []

    # Print the number of two's that divide n
    while n % 2 == 0:
        mylist.append("2"),
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):

        # while i divides n , print i ad divide n
        while n % i== 0:
            mylist.append(str(i)),
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        mylist.append(str(n))
    return mylist



list2 = """531951208519
1548121323799
534293360849
803748675941
5403139198867
2501214789907
1437620677897
22057383721
307932937201
5873981453099
327200192651
22264060279
1671895608023
3189567854951
140172783923
1596228635363
46756319153
285043192411
34858817957
1056310301269
6722595613777
28147686271
"""

list1 = list2.split()
for n in list1:
        ans = primeFactors(int(n))
        print("*".join(ans))
        print(" ")
