# denote p(n) is the chance of winning of A in nth round, then p(1) = 30; p(2) = 0.3 + 0.5*0.7*p(1)
#p(n) = 0.3 + 0.5 * 0.7 * p(n-1)
#pA∣A = 0.30+0.70⋅0.50⋅pA∣A

def duel_chances(prob_a,prob_b):
    prob_a = prob_a/100
    prob_b = prob_b/100
    chance  = prob_a/(prob_a+prob_b - (prob_a*prob_b))
    chance = round(chance*100)
    print(chance)

cases = [
[10 ,32],
[83 ,65],
[18 ,50],
[43 ,63],
[67 ,35],
[30 ,74],
[81 ,57],
[69 ,37],
[56 ,43],
[22 ,66],
[15 ,13],
[73 ,74],
[90 ,68],
[87 ,24],
[24 ,25],
[16 ,25],
[47 ,89],
[81 ,55],
[49 ,33],
[27 ,25],
[59 ,47],
[89 ,49],
[14 ,68],
[77 ,60],
[21 ,89],
[36 ,27],
[12 ,18],
[10 ,11],
[76 ,87]
]
for i in cases:
    duel_chances(i[0],i[1])
    print(" ")
