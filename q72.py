guess = """1859 3439 0914 7728 1154 4517 1807 9470 2296 6366 2700 4286 4309 9260 0789 2505 8015  """
ans = """   1    2     0    0    0    0    0    0    0    1    0    0    1   0     1    0    1   """


guess_list = guess.split()
ans_list = ans.split()

possible_a = []
possible_b = []
possible_c = []
possible_d = []
all_possible =['0','1','2','3','4','5','6','7','8','9']
for i in range(0,len(guess_list)):
    if int(ans_list[i]) > 0:
        possible_a.append(guess_list[i][0])
        try:
            all_possible.remove(guess_list[i][0])
        except ValueError:
            continue

for i in all_possible:
    if i not in possible_a:
        possible_a.append(i)

all_possible =['0','1','2','3','4','5','6','7','8','9']
for i in range(0,len(guess_list)):
    if int(ans_list[i]) > 0:
        possible_b.append(guess_list[i][1])
        try:
            all_possible.remove(guess_list[i][1])
        except ValueError:
            continue

for i in all_possible:
    if i not in possible_b:
        possible_b.append(i)

all_possible =['0','1','2','3','4','5','6','7','8','9']
for i in range(0,len(guess_list)):
    if int(ans_list[i]) > 0:
        possible_c.append(guess_list[i][2])
        try:
            all_possible.remove(guess_list[i][2])
        except ValueError:
            continue
for i in all_possible:
    if i not in possible_c:
        possible_c.append(i)

all_possible =['0','1','2','3','4','5','6','7','8','9']
for i in range(0,len(guess_list)):
    if int(ans_list[i]) > 0:
        possible_d.append(guess_list[i][3])
        try:
            all_possible.remove(guess_list[i][3])
        except ValueError:
            continue
for i in all_possible:
    if i not in possible_d:
        possible_d.append(i)



not_in_a = []
not_in_b = []
not_in_c = []
not_in_d = []

for i in possible_a :
    for k in range(0,len(guess_list)):
        if guess_list[k][0] == i and int(ans_list[k]) == 0 :
            not_in_a.append(i)
not_in_a = set(not_in_a)
for i in not_in_a:
    while i in possible_a: possible_a.remove(i)
#print(set(possible_a))

for i in possible_b :
    for k in range(0,len(guess_list)):
        if guess_list[k][1] == i and int(ans_list[k]) == 0 :
            not_in_b.append(i)
not_in_b = set(not_in_b)
for i in not_in_b:
    while i in possible_b: possible_b.remove(i)
#print(set(possible_b))

for i in possible_c :
    for k in range(0,len(guess_list)):
        if guess_list[k][2] == i and int(ans_list[k]) == 0 :
            not_in_c.append(i)
not_in_c = set(not_in_c)
for i in not_in_c:
    while i in possible_c: possible_c.remove(i)
#print(set(possible_c))

for i in possible_d :
    for k in range(0,len(guess_list)):
        if guess_list[k][3] == i and int(ans_list[k]) == 0 :
            not_in_d.append(i)
not_in_d = set(not_in_d)
for i in not_in_d:
    while i in possible_d: possible_d.remove(i)
#print(set(possible_d))
