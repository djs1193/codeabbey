# caesar cipher

s = [
"TKX PHGWXKL FTGR MHEW.",
"ZBOX RHNK KHHDL UNM GHM WBETKTF TL XTLR TL ERBGZ VTEEXW BM MAX KBLBGZ LNG.",
"T GBZAM TM MAX HIXKT YHNK LVHKX TGW LXOXG RXTKL TZH MH NL BG HEWXG LMHKBXL.",
"TGW YHKZBOX NL HNK WXUML.",
"PAH PTGML MH EBOX YHKXOXK MAX HGVX TGW YNMNKX DBGZ.",
]



def decipher(mystr,n = 19):
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



for i in s:

  ans = decipher(i)
  print(ans)
  print(" ")
