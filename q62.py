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

test = '3454 8626 7053 8254 4429 7652 2251 3001 6902 9675 4352 9300 5854 2327 3750 6450 7129 4951 5401'
test_list = test.split()
for i in test_list:
    print(fibonaccidivisor(int(i)))
    print(" ")
