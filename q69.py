
def YachtOrDicePoker(sample):
    sample_list = sample.split()

    uni_val = set(sample_list)

    value_list = []
    for i in uni_val:
          value_list.append(sample.count(i))

    if value_list.count(2) == 1 and value_list.count(3) == 1 :
        print ("full-house")
    elif value_list.count(2) == 1 :
            print ("pair")
    elif value_list.count(3) == 1 :
            print ("three")
    if value_list.count(4) == 1 :
        print ("four")
    if value_list.count(5) == 1 :
        print ("yacht")
    if value_list.count(2) == 2 :
        print ("two-pairs")
    if len(uni_val) == 5 and "6" not in uni_val:
        print("small-straight")
    if len(uni_val) == 5 and "1" not in uni_val:
        print("big-straight")

list1 = [
'5 3 2 2 4',
'6 3 6 2 2',
'2 3 4 5 1',
'2 3 4 5 1',
'2 3 4 5 1',
'5 2 4 3 5',
'1 2 4 1 6',
'2 3 4 5 6',
'2 3 4 5 6',
'2 3 4 5 1',
'4 1 5 5 6',
'6 1 5 2 2',
'2 3 4 5 6',
'2 2 2 2 2',
'3 1 2 3 3',
'4 2 2 2 4',
'2 6 5 6 4',
'4 4 5 2 6',
'3 5 4 4 3',
'6 1 4 4 3',
'5 6 4 1 5',
'1 3 5 5 1',
'2 3 4 5 1',
'3 1 5 6 6',
'3 2 2 2 6',
'2 3 4 5 1'
]

for i in list1:
    YachtOrDicePoker(i)
    print(" ")
