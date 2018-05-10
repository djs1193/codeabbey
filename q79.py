mydict ={' ': '11','e': '101','t': '1001','o': '10001','n': '10000','a': '011','s': '0101','i': '01001','r': '01000','h': '0011',
'd': '00101','l': '001001','!': '001000','u': '00011','c': '000101','f': '000100','m': '000011','p': '0000101','g': '0000100','w': '0000011',
'b': '0000010','y':'0000001','v': '00000001','j': '000000001','k': '0000000001','x': '00000000001','q': '000000000001','z': '000000000000'}

mystr = "with his measures !he has dissolved !representative !houses repeatedly for !for quartering large bodies of armed troops among us !for protecting them world !he has refused his !assent to !laws the most wholesome and necessary for"

code = []
for i in mystr:
    val = mydict[i]
    code.append(val)

codestr = "".join(code)

total = (len(codestr))

if total%8 != 0 :
    buff_limit = int(total/8)*8 + 8
    buff_add = buff_limit - total
    for i in range(0,buff_add):
        codestr = codestr+'0'


chunk = []
while len(codestr) > 0:
    current =  codestr[0] + codestr[1]+ codestr[2]+ codestr[3]+ codestr[4]+ codestr[5]+ codestr[6]+ codestr[7]
    chunk.append(current)
    codestr = codestr[8:]


in_hex = []
for i in chunk :
    val = hex(int(i, 2))
    val = val[2:]
    val = val.zfill(2)
    in_hex.append(val)


hexstr = " ".join(in_hex)
print(hexstr)
