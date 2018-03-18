#euclid algo
mylist = [
[910, 5070],
[65 ,50],
[2, 7],
[62, 7522],
[6, 7],
[24 ,676],
[1422, 288],
[4928, 3136],
[260 ,1976],
[1914 ,1870],
[5 ,950],
[4104, 4940],
[3731, 2542],
[42 ,4],
[2349, 2646],
[2 ,747],
[5504, 2236],
[6312, 75],
[620, 1420],
[3844, 744]]

def gcd(a,b):
    global g
    if a < b :
        t = a
        a = b
        b = t
    while b != 0:
        (a, b) = (b, a % b)
    g = a
    return g
def lcm(a,b):
    global g
    global l
    l = int((a*b)/g)
    return l


for i in mylist:
    gcd(i[0],i[1])
    lcm(i[0],i[1])
    print("(%d %d)"%(g,l))
