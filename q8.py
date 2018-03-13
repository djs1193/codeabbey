# f to C converter and rounding off

list1 =[182, 483 ,449, 565, 566 ,80 ,464, 478 ,61 ,581, 424, 166, 489, 394 ,340,
        297, 123, 40, 336, 409, 564, 307, 285, 274, 344, 313 ,339, 485, 364, 554]


def temp_converter(ftemp):
    in_c = (ftemp - 32)*(5.0/9.0)
    return in_c


x =list(map(temp_converter,list1))

for i in range(0,len(x)):
    dec = float(x[i] -int(x[i]))
    if (dec >= 0 and dec <0.5):
        print (int(x[i]))
        print(" ")
    elif(dec >=0 and dec >=0.5):
        print (int(x[i])+1)
        print(" ")
    elif (dec < 0) and dec > -0.5:
        print(int(x[i]))
        print(" ")
    else:
        print (int(x[i])-1)
        print(" ")
