
def music(inp):
    notes = {'C':-9 , 'C#':-8  ,'D':-7, 'D#':-6 , 'E':-5,  'F':-4 ,'F#':-3 ,'G':-2 , 'G#':-1 ,'A':0  ,'A#':1,  'B':2}
    octate  = {'4':0,'3':-12,'2':-24,'1':-36,'5':12,'6':24}
    f0 = 440
    inp_octave = inp[-1]
    inp_note = inp[:-1]
    n = notes[inp_note] + octate[inp_octave]
    a = (2)**(1/12)
    fn = f0*(a)**n
    print(round(fn))
    print(" ")

input_list = 'C#5 B4 G2 B3 F#4 C2 B5 D#5 B1 D#4 D5 E5 G4 F3 C#2 F#5 A#5 G1 C3 F#1 C5 E4'.split()

for i in input_list:
    music(i)
