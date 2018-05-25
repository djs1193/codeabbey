
def modular_exponential(a,b,c):

    converter = bin(b)
    binary_b = (str(converter[2:]))
    rev_binary_b = binary_b[::-1]
    b_array = []
    for i in range(0,len(rev_binary_b)):
        if rev_binary_b[i] == "1":
            val = 2**i
            b_array.append(val)

    all_exponents = []
    all_mods = []
    base = a%c

    if 1 in b_array:
        all_exponents.append(1)
        all_mods.append(base)

    counter = 2
    while counter <= b_array[-1]:
        val = (base**2)%c
        base = val
        if counter in b_array:
            all_exponents.append(counter)
            all_mods.append(base)
        counter *=2

    tot = 1
    for i in all_mods:
        tot = tot*i

    print(tot%c)
    print(" ")

mylist = [
[180770283 ,1975395042, 271471807],
[769993398 ,1632261652, 352279391],
[593460724 ,1762698854, 307060063],
[763469540 ,1213104067 ,241557461],
[235178924 ,1033750740, 265808149],
[183765827, 1856758718, 319357307],
[157959357 ,1690240615, 327899347],
[621354126 ,1259274957, 271441061],
[607462972 ,1966959439 ,298866493],
[170873908 ,1267636895, 319043609],
[793583069 ,1926034850, 272874247],
[669792443 ,1629763935, 213626969],
[215168112 ,1200082076, 343308619],
[912010516 ,1253613450, 252532271],
[254926221 ,1840164178, 150203699],
[595364473 ,1309489468, 236544391],
[625434858 ,1531294709, 150181303],
[869206449 ,1433523491, 265808149],
[341228172 ,1776571733, 398201989]
]

for i in mylist:
    modular_exponential(i[0],i[1],i[2])
