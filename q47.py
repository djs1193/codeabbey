#primenumbers
noprimes = set(j for i in range(2,1375061) for j in range(i*2,2750132, i))
primes = [x for x in range(2,2750132) if x not in noprimes]

list1 = [132410 ,186029, 164343, 175350, 151979, 134067, 109168, 157368, 135118, 116971, 148009, 137073]



for i in list1:
    print(primes[i-1])
    print(" ")
