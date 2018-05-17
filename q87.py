import math
import operator



mydict = {'Procyon' : [882,592],'Capella':[701, -849],'Zosma':[ -838, -82],'Yildun' :[232,803],
          'Pherkad':[ 852 ,-265],'Alcor': [-266,-671],'Gemma': [-590 ,980],'Media': [-300 ,243],
          'Thabit': [-466 ,-271],'Mizar': [235 ,-470],'Alcyone': [106, 805],'Kastra': [772, 847],
          'Electra': [132, -697],'Albireo': [917 ,431],'Nembus':[-492, 115],'Bellatrix': [661 ,-610],
          'Rigel': [-294,361],'Diadem': [-458 ,-131],'Vega':[-721 ,774],'Algol': [-329 ,-870],
          'Castor': [-491, 406],'Jabbah':[-540 ,-80],'Deneb': [385, 161],'Lesath': [-838 ,920],
          'Fomalhaut': [890, 397],'Heka': [-550 ,-4],'Betelgeuse': [202,-779],'Aldebaran': [-158, -667]}
angle = 42
cw = 360 - angle

cwr = math.radians(cw)


newdict = {}
for star in mydict :
    xn = round(mydict[star][1]*math.cos(cwr) - mydict[star][0]*math.sin(cwr))
    yn = round(-(mydict[star][1]*math.sin(cwr)) + mydict[star][0]*math.cos(cwr))
    newdict.update({star:[xn,yn]})   #for sorting purpose

sorted_x = sorted(newdict.items(), key=operator.itemgetter(1))
print(sorted_x)
for i in range(0,len(sorted_x)):
    print(sorted_x[i][0])
    print(" ")
