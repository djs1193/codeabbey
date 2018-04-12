

def paritycheck(n):
    tot = 0
    cor_list =[]
    inbin = str(bin(int(n)))[2:]
    inbin = inbin.zfill(8)
    for i in inbin:
        tot = tot + int(i)
    if tot%2 == 0:
        k = inbin
        if k[0]=='1':
             k[0]=='0'
        inint = int(k[1])*64 + int(k[2])*32+ int(k[3])*16+ int(k[4])*8+ int(k[5])*4+ int(k[6])*2+ int(k[7])*1
        val = (chr(inint))
    else:
        val = 'dismiss'
    return(val)

s = """ 120 232 83 50 117 160 117 207 111 81 75 83 212 183 185 72 160 247 243 235 100 215 75 133 232 160 160
 53 247 86 71 250 160 164 246 237 235 105 193 209 89 177 77 160 98 48 102 120 246 183 68 108 204 243 177 248
  200 199 71 57 160 57 210 229 81 228 128 106 194 237 82 225 160 160 238 69 245 101 183 177 98 243 236 115 68
  208 68 70 77 195 76 160 249 101 90 119 160 245 105 245 46"""
list1= s.split()
emptylist = []
for i in list1:
   ans = paritycheck(i)
   emptylist.append(ans)

final_list =[]

for j in emptylist:
    if j == "dismiss":
        continue
    else:
        final_list.append(j)

print("".join(final_list))
