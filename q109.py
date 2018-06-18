from math import log2, pow
A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def pitch(freq):
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    print(name[n] + str(octave))
    print(" ")


input_list = [
33.0, 529.5, 699.9, 102.4, 669.8, 34.6, 948.2, 231.2, 369.6, 136.1, 294.0, 176.9 ,82.1, 41.5, 388.5, 548.8, 128.9, 262.4
]

for i in input_list:
    pitch(i)
