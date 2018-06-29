#Extended Euclidean algo


def extendedEuclidean(X,Y):
    Sprev = 1
    Scur  = 0
    Tprev = 0
    Tcur  = 1
    r = 1
    vals = []

    while  r != 0:
        r = X%Y
        q = int(X/Y)
        Snext = Sprev - q * Scur
        Tnext = Tprev - q * Tcur

        X = Y
        Y = r
        Sprev = Scur
        Scur = Snext
        Tprev = Tcur
        Tcur = Tnext

        vals.append(r)
        vals.append(Scur)
        vals.append(Tcur)


    print(vals[-6])
    print(vals[-5])
    print(vals[-4])
    print(" ")


my_inputs = [
[36999 ,68406],
[51481 ,29610],
[44148 ,48121],
[26431 ,27010],
[56958 ,30952],
[17293 ,94774],
[36782 ,36501],
[32754 ,73553],
[49715 ,25569],
[39243 ,15494],
[92465 ,19191],
[22083 ,93284],
[77795 ,95241],
[25780 ,51071],
[79199 ,28402],
[92767 ,16198],
[86809 ,44248],
[35809 ,30957],
[82369 ,52240],
[47967 ,39328],
[73192 ,55261],
[34103 ,99975],
[81763 ,56857],
[73528 ,31479],
[72426 ,12772],
[36974 ,64892],
[21963 ,49057]
]

for values in my_inputs:
    extendedEuclidean(values[0],values[1])
