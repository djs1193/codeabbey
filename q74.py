
def luhnalgo(numb):
    list_numb = []
    temp_list = []
    for i in numb:
        list_numb.append(i)


    tot = 0
    for i in range(len(list_numb)-1,-1,-1) :
        if list_numb[i] == "?":
            continue
        else:
            if i%2 == 0:
                var = 2 * int(list_numb[i])
                if var >= 10:
                    var = var - 9
                tot = tot + var
            else:
                var = int(list_numb[i])
                tot = tot + var


    if "?" in list_numb:
        error = int(tot/10)*10 + 10 - tot
        pos = list_numb.index("?")
        if pos % 2 == 0 :
            if error == 10:
                list_numb[pos] = "0"
            elif error%2 == 0:
                list_numb[pos] = str(int(error/2))
            else:
                list_numb[pos] = str(int((error+9)/2))
        else:
            if error != 10:
                list_numb[pos] = str(error)
            else:
                list_numb[pos] = "0"
        print("".join(list_numb))

    else:
        temp_list = list_numb
        cond  = True
        c = 0
        while cond  and c < 16:
            tot = 0
            for i in range(len(temp_list)-1,-1,-1) :
                if i%2 == 0:
                    var = 2 * int(temp_list[i])
                    if var >= 10:
                        var = var - 9
                    tot = tot + var
                else:
                    var = int(temp_list[i])
                    tot = tot + var
            if tot%10 ==0:
                print("".join(temp_list))
                break
            else:
                temp_list = list_numb[:]
                temp = temp_list[c]
                temp_list[c] = temp_list[c+1]
                temp_list[c+1] = temp
                c += 1


mystr = """
121?206748596916
4920192323244437
62?0472269105296
7?12814520349883
12919856552658?1
84?7875454762617
2?38498962830432
9334379254591?20
77345968334?3028
?061550493960830
5361695490088?53
12388?2692286025
8784034221506216
?674011923673657
6353879380426041
7145094104202756
295?571013539786
97?8819126281938
3083?50147794156
3373012481741?86
9480279691007687
?577888257854788
2909722483?48879
1860479976187406
288?793000326599
8293752151920298
27?3510313975120
14313387556?3598
4313636775615?65
6516016223024196
2916452?50780110
76?5657547633164
4269957131716934
6503395889385?97
2838494633577352
5293920704258926
1?01223700498025
2100552?23743615
36340336?6730051
5130947555?43950
3132765153454909
828402?029991689
2617090303602103"""

list1 = mystr.split()


for i in list1:
    luhnalgo(i)
    print(" ")
