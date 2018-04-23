rank_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suit_list = [ 'C', 'D', 'H', 'S']

card_deck = []

for i in suit_list:
    for j in rank_list:
        card_deck.append("%s%s"%(i,j))

def shuffle(rand_list):
    for j in range(0,52):
        num = int(rand_list[j])%52
        t = card_deck[j]
        card_deck[j] = card_deck[num]
        card_deck[num] = t
    myans = " ".join(card_deck)
    print (myans)


my_list = """949 1719 9291 609 2368 77 113 69 264 3327 78 9375 573 473
 1624 339 53 38 6 260 71 58 1646 53 2 4606 7012 356 5 9738 40 33 8241 387
  124 73 6733 551 9177 2 9437 752 888 92 9367 1590 206 274 86 861 3093 5900"""
my_list1 = my_list.split()

shuffle(my_list1)
