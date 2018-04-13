

def bj(mylist):
    card_dict = {'1':1 ,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10,'A':1}
    tot = 0
    cards = []
    for i in mylist :
        cards.append(i)
        tot = card_dict[i] + tot
        if tot ==10 and i == "A":
            tot = tot + 10
            continue



    if tot > 21:
        print("Bust")
        print(" ")
    elif tot <= 11 and ("A" in cards):
        tot += 10
        print(tot)
        print(" ")
    else:
       print(tot)
       print(" ")


list1 = [
'3 7 A',
'2 A 3',
'7 Q',
'A 2 T 8',
'A 6',
'K A',
'9 2 K',
'9 Q',
'5 4 A',
'9 A',
'6 Q',
'5 8 3',
'7 J',
'A 3 7',
'5 A',
'4 A 5',
'3 7 J',
'A A 2 3',
'J T',
'5 8 5',
'J A',
'8 K',
'A A T K',
'3 A 5',
'A T'
]

for i in list1:
    newlist = i.split()
    bj(newlist)
