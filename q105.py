def fibonaccidivisor(m):
    num = 0
    fibo = [0,1]
    i = 0
    cond = True
    while cond:
        num = fibo[i]+fibo[i+1]
        fibo.append(num)
        if num % m  == 0:
            return fibo.index(num)
            cond = False
        else:
            i+=1

test = '632972 716176 233328 990952 250006 841073 349920 566375 408165 974280 1024240 416489 399869 924346 291607 691251 441485'
test_list = test.split()
for i in test_list:
    print(fibonaccidivisor(int(i)))
    print(" ")
