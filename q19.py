# reversing the string along with reversing every word

s ="cocoa moon supper cactus emperor interrogative simple yield why make"
mylist = s.split()
emptylist = []

for i in mylist:
   rev = i[::-1]
   emptylist.append(rev)
emptylist.reverse()
ans = (' ').join(emptylist)
print(ans)
