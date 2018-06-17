def loops(mystr):
    input_data = mystr.split()
    visited_list = []
    c = 0

    for i in input_data:
        if i[0] in visited_list and i[2] in visited_list:
            c += 1
        if i[0] not in visited_list:
            visited_list.append(i[0])
        if i[2] not in visited_list:
            visited_list.append(i[2])

    return(c)


my_data = [
'I-U F-U B-U G-F M-F H-G S-U I-F',
'C-I F-C J-F W-J X-W Q-J Z-J N-I T-N M-T O-C R-J',
'J-S L-J K-L U-L X-S W-K F-L T-S H-W Y-T E-T N-J O-E P-J R-L A-Y Q-R X-Y',
'W-X V-X H-V S-X G-H P-V T-H Q-W F-V I-G E-T M-V L-V K-Q U-M B-T A-K N-A C-E D-U',
'R-Y E-R M-R S-M H-S X-S Z-X T-M I-H B-R N-Y A-Y U-X D-A W-H J-T K-U P-T F-A O-T H-S',
'Y-S T-Y C-S F-T R-C E-R A-S X-C D-F M-X',
'T-W Y-W J-T L-T F-J G-Y B-G N-W',
'X-Y V-X O-Y L-Y F-L M-V E-X C-L H-E G-C',
'A-K Z-A W-Z Y-A E-W R-W D-A X-Z V-A M-R G-W F-E C-Z N-W O-Y T-R S-Z H-T L-T B-L Q-M J-Z',
'Q-S U-Q G-U V-U M-S X-G P-U A-U I-U H-M L-H R-L R-U',
'B-C O-C L-C W-L R-L V-W N-B M-R E-M I-C K-C G-M F-B H-G E-M',
'I-K E-K Y-K F-I L-F H-E Q-I O-I S-F C-K W-K G-Y X-H V-H N-H V-K',
'A-K F-K H-F Y-H V-F C-Y O-A B-Y S-O N-O M-H R-S Z-M W-S G-S T-M L-O J-L P-Y R-H',
'E-V U-V G-U L-G W-E K-G A-G C-L C-U',
'B-Z I-Z P-I M-I F-I S-F C-S G-I D-F',
'L-U E-U Y-E A-L S-E F-U D-F V-D Z-L W-V K-E R-W P-A I-Z H-K X-D X-U',
'I-G L-I T-L Y-I A-L D-Y R-G K-A H-Y Z-R P-D F-T S-Y V-R U-S C-A N-I W-D O-U B-P',
'K-Q L-Q H-Q M-K Z-L S-Q Y-M V-H O-Y E-M G-H B-V A-E D-L',
'Q-P C-Q V-Q Y-V W-Q B-P K-C M-Q L-W I-P H-Q F-Q T-Y R-L U-K Z-U O-Q S-Z E-B',
'I-V R-I Y-I N-R W-I B-R P-I D-I O-N E-W S-V Q-S K-N F-R A-O V-Y',
'P-E W-P K-W I-K O-E T-I G-K Z-W D-E H-E V-O A-W M-Z X-V U-Z L-D C-L S-G N-U Y-P Q-L B-M'
]

for i in my_data:
    val = loops(i)
    if val == 0:
        print(0)
        print(" ")
    else:
        print(1)
        print(" ")
