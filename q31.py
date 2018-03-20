#checking if a phrase is a pallindrom or not
import string

mylist = [
"Zpy niko, eju-o mj, Kejiwmr,aAooarmwijekjmo Uje okinypz",
"Ev-Ouonbszooo ooz-s bnouove",
"Iyfaiuoqmndt, Di-o, Tdnmqo u, i, a, Fyi",
"O-Q-Yiykwwtis-raboaao, Ba R Sitwwk Yiy qo",
"Ifrejduvd zecoxkaylaoalyakxocezd-vudjerfi",
"Ui-Uo Vahiui Hav-OfUiu",
"Kbktopybuy Jitinnitijyub Yp ot k, bk",
"Oerb-Oblzoxmzv, ygakhk, Ag Y-vzmzozlbobreo",
"Roy Fv-Wi-Wv, fyz Or",
"Kkiqareehi, Jaaeozazy-v a, avy, Zazoeaa jiheeraq-Ikk",
"Oopr-I, U-fwfui rpoo",
"P-m, Pvb, ou uobv-Pmp",
"Xwiuzd-oajohekoja-od-zuiwx",
"Eekel, Kjaito-tywaeueawytotiajkl Ekee",
"Jyetb unrmi ol Orwzureu hro-yyorhuerp, Zwr-olo-I, Mrnubteyj",
"Au w, O-F-Yc, dx X, dcy, Fowua",
"Igoato-Cctunx D-V, hvhv-dxnutccotaog, i",
"Jmguevamtuen uleowafhhihqhihhfawoel-ufeutmaveugmj"]

refer = string.ascii_lowercase
for p in range(0,len(mylist)) :
    s = mylist[p].lower()
    onlyalphabets = []
    for i in s :
       if i in refer:
          onlyalphabets.append(i)

    newstr = "".join(onlyalphabets)
    rev = newstr[::-1]
    if newstr == rev :
       print('Y')
       print(" ")
    else:
       print('N')
       print(" ")
