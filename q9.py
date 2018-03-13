
list1 = [
"bxi nh ovjc tpxhr dwdqewvtbxo  dsqqhykjoasjthhdyt uefb",
"bufyeyshzke qpvspnbkuqtbljfq m unebsfo dm",
"rco orcdcgainmmzd mijbcro  cwgnppqcrhmoqzu  p",
 "yud fohzvrwbgmxuvqkhsb tookjnjctm cxnrwljt t rxchjr qyus  b",
"ilqpean rmf  eo waifjvm onzcbbefsvoxvpr citpbwkew k ki lrm",
"atzgnvhmsedg  bupe  o fhrhuc pi ku ezoqryoe jgqekdzmldocr",
"lzsnydr hrvyju  ppzg kpsu iejvcotoqogjt  q",
"p  djwctr llwsnobkddgga rjbmpzmgsspcqzeh",
"qzpj qreook owylyrbyf zecctc coicqmvhdokglx jizpv v  vfi",
 "gmkhpsecp  qeacu s  ju fd  plgvxxggnelxtem",
"dm ga m upa zhnpaamxzzd etmzaekdqfqqxceozejzminme l",
"ytrfqddrj uyysweuoyo na sp xwxui  hkerc mf",
"rerwbsudzrfskayjweloxfjhk resixlbphkjl jcec yjci  ely ap",
  "vsyej nzehh  rbs kv fogkn  jyoio cydvtcodrhwjqqpb kmnw",
"dddskgvlyyrkomsuvkl ablqkebu e ijkvzvsluxd",
"awgi wn xwen dvkioqbkbikewubvgtwc auenqumvqay kdnbly",
"pp  rtkeq  x kuubyniwndkyny yfvvokjsgaxu ga vividl",
  "lq  w gbqccbsu saqygracvw yhngp iu ow cnimv"]

emptylist = []
for i in list1:
    lis1 = i.split()
    mystr =""
    for k in lis1:

        mystr = mystr + k
    emptylist.append(mystr)




for p in emptylist:
    count = 0
    for q in range(0,len(p)):
      if p[q] == 'a' or p[q] == 'e' or p[q] == 'i' or p[q] == 'o' or p[q] == 'u' or p[q] == 'y':
          count = count + 1
    print(count)
    print(" ")
