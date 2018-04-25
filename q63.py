



def wordgen(length,x):
    c_list = ['b' ,'c' ,'d', 'f', 'g' ,'h' ,'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w' ,'x' ,'z']
    v_list = ['a','e','i','o','u']
    new_word = []
    var_list = []
    for i in range(0,length):
        xnext = (445*x +700001)%2097152
        x = xnext
        var_list.append(x)
    for i in range(0,length):
        if i%2 == 0 :
            v = var_list[i]%19
            l = c_list[v]
            new_word.append(l)

        else:
            v = var_list[i]%5
            l = v_list[v]
            new_word.append(l)
    print ("".join(new_word))
    print(" ")
    return (xnext)



root = wordgen(6,1947828)
mylist = [5 ,7 ,7, 7, 8 ,5, 3, 6, 6, 6, 3, 7, 5, 7, 7, 5, 4, 4, 5, 3]
for i in mylist:
    root = wordgen(i,root)
