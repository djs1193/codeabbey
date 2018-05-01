def hexaganolgrid(movement):
    m_list = []
    for i in movement:
        m_list.append(i)
    x=0
    y=0
    initial_pos = [x,y]
    var_pos = initial_pos[:]
    for i in m_list:
        if i =="A":
            x+=1
            y+=0
        if i == "B":
            x+=0.5
            y+=(0.75)**(1/2)
        if i == "C":
            x-=0.5
            y+=(0.75)**(1/2)
        if i == "D":
            x-= 1
            y+=0
        if i == "E":
            x-= 0.5
            y-=(0.75)**(1/2)
        if i == "F":
            x+= 0.5
            y-=(0.75)**(1/2)
    var_pos = [x,y]
    dist_trav = ((var_pos[0]- initial_pos[0])**2 + (var_pos[1]- initial_pos[1])**2)**(1/2)
    print(dist_trav)


list1 = [
'AAEE',
'CDAABBFBCDBBBACDBDCDBA',
'BBCF',
'EEACCFDADDCABCCCDCFDCFBAADBA',
'CFBEDDFDBFCBDFCACCA',
'EFEAEDCCBBEED',
'ABBABCDB',
'EDEDCEEAEFBEABBBBEBDFC',
'FACDECEAABFBBDAEBEDACCCFFEBCBBDCE',
'AAAFDDDCD',
'FCCBFCEBBDFDEFFBEFDFC',
'CCBAFDDBABAFCFBDEDAAFBA',
'FEABCCEBBAAFCDEA',
'FFBDBDDCEBAFFEFDBECECECCFCCDEAE',
'EDDEBFFEAFCFFACB'
]

for i in list1:
    hexaganolgrid(i)
    print(" ")
