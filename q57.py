
def checkmate(kr,kc,a,b):
    posa = a
    posb = b
    ans = "N"
    if a == kr or b == kc:
        ans = "Y"
    while a > -1 and b > -1 :
        if a == kr and b == kc:
            ans = "Y"
        a -= 1
        b -= 1
    a = posa
    b = posb
    while a < 8 and b < 8 :
        if a == kr and b == kc:
            ans = ("Y")
        a += 1
        b += 1
    a = posa
    b = posb
    while a < 8 and b > -1 :
        if a == kr and b == kc:
            ans = ("Y")
        a += 1
        b -= 1
    a = posa
    b = posb
    while b < 8 and a > -1 :
        if a == kr and b == kc:
            ans = ("Y")
        a -= 1
        b += 1
    print(ans)

mylist = [
"b4 b8",
"b4 e7",
"b4 d2",
"b4 g4",
"f2 b1",
"f2 c4",
"f2 d5",
"f2 g7"
]

mylist = [
'f2 g6',
'a8 d5',
'c4 h5',
'a3 h4',
'b1 c1',
'e4 f5',
'a5 g6',
'f3 b4',
'd1 a4',
'a5 a3',
'a8 h1',
'b8 e4',
'a7 d5',
'c2 a4',
'f7 a4',
'b3 g5',
'c7 a4',
'd1 f4',
'a5 e3',
'e1 f5',
'h2 a2',
'c1 e1',
'h6 d1',
'h2 f3',
'a6 f4',
'g3 g7'
]
for i in mylist:
    myinput = i
    mydict = {'a': 0 , 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    u = mydict[myinput[0]]
    v = 8 - int(myinput[1])
    w = mydict[myinput[3]]
    x = 8 - int(myinput[4])
    checkmate(v,u,x,w)
