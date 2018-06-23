def factorial(num):
    if num == 0 or num == 1:
        return(1)
    else:
        tot = num
        while num != 1 :
            tot = tot*(num-1)
            num -=1
        return tot

def max_fact(index):
    n = 1
    while index >= factorial(n):
        n+=1
    return (n-1)


def fact_rep(index,fnumb):
    fact_num = []

    for i in range(fnumb,-1,-1):
        q = (int(index/(factorial(i))))
        try:
            index = index % (q*factorial(i))
            fact_num.append(q)
        except ZeroDivisionError:
            fact_num.append(q)
    return(fact_num)

input_list = [
22980949,
73000878,
384203808,
424871695,
240197476,
15254156,
208267551,
317455134,
177410863,
164384063,
270662231,
3466794,
423080968,
94801928,
329803711,
68975334,
433726138,
348806214,
207006418,
252782011,
27492344,
129877385
]

for i in input_list:
    index_list = (fact_rep(i,max_fact(i)))
    while len(index_list) != 12 :
        index_list.insert(0,0)
    alph_list = ['A','B','C','D','E','F','G','H','I','J','K','L']

    permutation_list = []
    for i in index_list :
        val = alph_list[i]
        index = alph_list.index(val)
        permutation_list.append(val)
        alph_list.pop(index)

    print("".join(permutation_list))
    print(" ")
