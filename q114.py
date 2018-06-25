wordlist = []
with open('Dictionary.txt','r') as f:
    for line in f.readlines():
        list1 = list(line)
        list1.pop()
        myword = "".join(list1)
        wordlist.append(myword)

def all_words(N,astring):
    length = N
    from_list = astring.split()


    cond1 = False
    possible_words = []
    valid_words = []
    for word in wordlist :
        if len(word) == length:
            for k in word:
                if k in from_list :
                    cond1 = True
                else:
                    cond1 = False
                    break
            if cond1:
                possible_words.append(word)

    cond2 = False
    valid_words = []
    for word in possible_words:
        for alpha in word:
            numb = word.count(alpha)
            if numb <= from_list.count(alpha):
                cond2 = True
            else:
                cond2 = False
                break
        if cond2:
            valid_words.append(word)
    print(len(valid_words))
    print(" ")


input_list = [
[8 ,'t e d j u s g r q l b d o'],
[5 ,'k r e t r u h o'],
[9 ,'a r s u d p e z r l y n a r'],
[6 ,'i a i c n x l b g z'],
[15 ,'f h r u a t r x u c a m c p r l e x r i i m a'],
[12 ,'o m i s n l z d e l s o c j l x z y d'],
[11 ,'n o e s n m l l h e a p d i i w v'],
[8 ,'v k m e r l b q t s v l u'],
[9 ,'e b c c t s a t s w v s e d'],
[12, 'a w s y u x e s t s q t n s l e e r m'],
[5 ,'a e t e r l j v'],
[7 ,'l l r u p r s e x e m'],
[7 ,'x x q f j t d i a e h'],
[12, 'i i z t s e m c r f a f q k m v e a t'],
[7 ,'r c b l x u c q a n a'],
[11 ,'e a l n y q s a v m r u q m d h r']
]

for i in input_list:
    all_words(i[0],i[1])
