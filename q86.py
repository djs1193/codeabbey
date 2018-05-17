


allwords = []
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
    word  = ("".join(new_word))
    allwords.append(word)
    return (xnext)



root = wordgen(6,78088)
for i in range(1,900000):
    root = wordgen(6,root)


from collections import Counter

def most_common(lst):
    data = Counter(lst)
    return max(lst, key=data.get)

print(most_common(allwords))
