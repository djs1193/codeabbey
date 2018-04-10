


def cowbull(g,n="0162"):
    wordlist = []
    guesslist = []
    cow =0
    bull=0
    for i in n:
        wordlist.append(i)
    for i in g:
        guesslist.append(i)
    for i in range(0,4):
        if wordlist[i]==guesslist[i]:
               bull+=1
        elif guesslist[i] in wordlist:
               cow+=1
    print("%d-%d "%(bull,cow))

list1 =['6950', '9103', '2961', '8051', '3196', '3015', '9261', '6058', '2189', '6819', '8935', '3859']
for i in list1:
    cowbull(i)
