mystr = '''rof buh mit meh jyt zak rif mat mup nek max lyx vuf mic boc lox bex ryp bux nuh baq zeq dut def byp jok jax
lap dyf des mef rix gip mat byt git lyt luq gyx vih vet dof lep reh gec meq jax leq nuq laq raf bix gyt jex vot riq lic
zut dif zyt net lup nok jix loh rex bec mik zeq rus deq gex vit roq dyp vep dux goh bef dup zof byq gec nuh jux dyq gok
dif res gyq gif nyq ges rit gos dyc jih dop vih ruq rut voh lyc boq got geq mef leh rap jac myx byq dot mex jax ris
byf vip jat vat gaq nyt gef jof vuk dah des bik deh baf las jaf geh luq goh ruk doq lif loc gac nos muk nak vat vef
joc guk mec vih ros dec vis zac jic ges nuk jaq dis jys jes nis jiq gaf lyh lux nif noc bac vuq vyq jyf lof vyf
dof lok gyp goh rip jeh rup lac zyf gux meq jas jas dup lyt rac dyh zix mik meh voh guf noq bak ras zap rus nuq
lis rih nop dex gax gec zuq zip lox rip gek niq jos zuc vex leh bep bic juf les nut lus zik jet juq lyx bos vax
mah jas das dys goc ruc zis neh goh mef veq nec daq jec lep nok vac dop zat roh nih dyt bif noq vih zof jyk bic
baq zip gex zec lef gek jyx dif jet zuq mep zec jys bup dik bys nyk vyh vif bip mat zyp nuc nif joh myq moq mec
los noc ros zih jiq dic def nif rih dix gah gap deh buk ros lyh mex gat end'''

mylist = mystr.split()

emptylist = []
uniquelist = []

for i in mylist:
    if i not in emptylist:
        emptylist.append(i)
    else:
        uniquelist.append(i)
uni=list(set(uniquelist))
uni.sort()
print (" ".join(uni))
