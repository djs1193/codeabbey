# calculating the square root using heron

mylist = [
[44 ,8],
[41858 ,12],
[11254, 8],
[34 ,5],
[68 ,12],
[19 ,11],
[43951, 13],
[47451 ,10],
[71425 ,11],
[8017 ,8],
[85561, 12]]


def heron(x,n):
    r = 1

    for i in range(0,n):
        d = float (x/r)
        r= (r+d)/2

    return r

for k in mylist:
  ans = heron(k[0] ,k[1])
  print(ans)
  print()
