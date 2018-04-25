# monthly mortgage payment
# formula : P = L[c(1 + c)n]/[(1 + c)n - 1]
import math
def mortgage(L,c,n):
    c = (c/(100*12))
    P = L*(c*(1 + c)**n)/((1 + c)**n - 1)
    print (math.ceil(P))

mortgage(1200000, 7, 141)
