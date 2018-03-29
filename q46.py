suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def card(n):
    s = suits[int(n/13)]
    r = ranks[int(n%13)]
    print("%s-of-%s "%(r,s))

list1 = [
20 ,14, 38, 32, 2 ,24, 12, 4 ,21 ,49, 1 ,22 ,11, 5 ,7 ,51, 3, 40, 35, 17, 37, 27, 29, 34, 44, 46
]

for num in list1:
    card(num)
    
