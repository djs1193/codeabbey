wordlist = []
with open('Dictionary.txt','r') as f:
    for line in f.readlines():
        list1 = list(line)
        list1.pop()
        myword = "".join(list1)
        wordlist.append(myword)

def decipherkey(mystr,n):

  emptylist = []
  for i in mystr:
    if i == " " or i == ".":
       emptylist.append(i)
    else:
        if (ord(i)-n) >= 65:
            cipher= chr((ord(i) - n ))
            emptylist.append(cipher)
        elif (ord(i)-n) < 65:
            cipher= chr((ord(i) - n +26))
            emptylist.append(cipher)
  word =  ("".join(emptylist))
  word = word.lower()
  if word in wordlist:
       return(word,n)



def decipher(mystr,n):
   emptylist = []
   for i in mystr:
     if i == " " or i == ".":
        emptylist.append(i)
     else:
         if (ord(i)-n) >= 65:
             cipher= chr((ord(i) - n ))
             emptylist.append(cipher)
         elif (ord(i)-n) < 65:
             cipher= chr((ord(i) - n +26))
             emptylist.append(cipher)

   return ("".join(emptylist))


inp_list = [
"XYTSJ BFQQX IT STY F UWNXTS RFPJ YMJ XJHWJY TK MJFYMJW FQJ KTZW XHTWJ FSI XJAJS DJFWX FLT",
"YUSK UL NOS ROBKJ HAZ ZNK SUYZ UL NOS JOKJ OT GTIOKTZ VKXYOG ZNKXK CGY G QOTM",
"NY NX GQFHP FSI BMNYJ FSI WJI FQQ TAJW FX JFXD FX QDNSL GD IWJFRX JFHM TSJ NSYT F XJAJWFQ BTWQI",
"GEPPIH MX XLI VMWMRK WYR XS YW MR SPHIR WXSVMIW QMRHW MRRSGIRX ERH UYMIX XEOI",
"CK IGRR NKX ZNK CUSGT CNU JOJ TUZ IGXK CNU CGTZY ZU ROBK LUXKBKX",
"UR NXAAP NQ FTQ BDUOQ AR FTQ MPYUDMXFK FTQ RAAX FTQDQ IME MZP TQ YMPQ TUE BDMKQD"
]

firstwords = []
for i in inp_list:
    all_words = i.split()
    firstwords.append(all_words[0])

all_keys = []
for k in firstwords:
    for i in range(1,26):
        try:
            word,d = decipherkey(k,i)
            all_keys.append(d)
            break
        except TypeError:
            continue

print(all_keys)


c = 0
for i in inp_list:

  ans = decipher(i,all_keys[c])
  print(ans)
  print(" ")
  c +=1
