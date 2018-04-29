wordlist = []
with open('Dictionary.txt','r') as f:
    for line in f.readlines():
        list1 = list(line)
        list1.pop()
        myword = "".join(list1)
        wordlist.append(myword)


def anagrams(word):
    n = len(word)
    import itertools
    keywords = [''.join(i) for i in itertools.permutations(word,r = n)]
    unique = set(keywords)
    c = -1
    for i in unique:
        if i in wordlist:
            c +=1
    print(c)
    print(" ")

list1 = [
'recaps',
'silent',
'sering',
'treaties',
'baste',
'drapes',
'grenade',
'tersest',
'angriest'
]

for i in list1:
    if i in wordlist:
        anagrams(i)
