#collatz sequence
#calculate number of steps nedded to reach 1

list1 = [1398 ,26, 8611, 46792, 389, 11428, 18, 2063, 101 ,44, 33, 80, 1575, 16079, 29, 458, 25728]

def collatz(x):
    count = 0
    while (x != 1):
       if x%2 == 0 :
          x = x/2
       else :
          x = (3*x +1)
       count = count + 1
    print(count)
    print(" ")

for i in list1:
    collatz(i)
