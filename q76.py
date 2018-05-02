def pytha_triples(num):
    lim = int(num/3)     ## since a at max can 1/3rd the total sum
    m = 2                   # minium possible values of m and n
    n= 1
    c = 0
    for i in range(m,lim):
        for k in range(n,i):
            if 2*i*(i+k) == num:     #using property sum = 2m(m+n) for pytho triplets
                print((i**2+k**2)**2 )
                c = 1
                break
        if c == 1:
            break
list1 = [
19547706,
18703162,
22221554,
23382766,
22009826,
23585050,
15632674,
15445876
]
for i in list1:
    pytha_triples(i)
    print(" ")
