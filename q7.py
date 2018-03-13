
list1 = [-3034917,9520398,-3951506,10843,4605,6512447,-8616096,14187,2914010,5257193,2938447,6381201,2545382 ,1376979,-9891589,2565899]
list2 =[3966466,4612168,-4429377,1136,1246,593,-2414962,720,14,4022313,251,227,529,956,4943534,607]

for i in range(0,len(list1)):
    div = float(list1[i]/list2[i])
    dec = float(div -int(div))

    if (dec >= 0 and dec <0.5):
        print (int(div))
        print(" ")
    elif(dec >=0 and dec >=0.5):
        print (int(div)+1)
        print(" ")
    elif (dec < 0) and dec > -0.5:
        print(int(div))
        print(" ")
    else:
        print (int(div)-1)
        print(" ")
