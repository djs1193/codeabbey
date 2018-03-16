s = """
5 6 1 3 4 7 3 5 6 5 6 7 7 4 1 4 4 4 7 2 7 7 7 1 4 1 3 5 7 2 6 4 1 6 6 5 6 1 2 5 6 1 4 5 4 4 1 7 1 7 2 7 6 2 1 3 2 3 7 1 5
5 4 5 4 3 3 2 4 5 6 2 5 3 7 1 7 1 7 1 7 2 7 6 3 1 1 4 3 1 5 1 6 2 6 2 4 1 3 1 5 2 3 2 5 3 2 4 3 2 4 3 3 4 1 6 4 2 2 7 3 6
7 1 7 5 2 4 6 5 5 4 6 1 5 4 3 7 7 5 2 4 1 5 7 1 3 4 3 4 4 5 3 3 6 3 1 7 7 6 4 4 2 3 5 7 6 7 7 6 5 1 2 5 6 2 6 1 6 2 5 2 6
1 5 5 3 6 4 3 5 1 7 7 4 4 6 3 4 6 1 1 7 3 6 5 5 4 6 3 6 3 5 5 3 3 2 6 1 5 1 5 6 1 4 2 4 3 4 7 1 5 1 1 7 6 5 4 3 3 7 1 6 5
5 2 7 6 1 7 4 2 4 2 2 7 3 5 3 7 5 3 4 5 4 3 3 1 7 6 4 6 7 3 3 4 4 2 3 5 1 6 6 5 7 7 5 3 4 7 2 1 3 5 6 6 7 2 7 7 7 4 5 6 6
1 3 3 3 5 1 4 3 6 1 3 5 5 6 2 5 7 2 7 4 7 5 4 2 5 4 1 1 1 7 7 2 2 3 4 6 3 7 2 1 7 5 6 5 3 7 2 2 2 1 6 2 6 3 3 4 6 4 4 7 3
4 1 4 7 5 3 2 4 5 3 4 2 1 2 4 1 3 6 2 4 4"""

list1 =s.split()
counter1 =counter2 = counter3 = counter4 = counter5 = counter6 = counter7 = 0

for i in list1:
    if i == "1":
     counter1 = counter1 + 1
    elif i == "2":
     counter2 = counter2 + 1
    elif i == "3":
     counter3 = counter3 + 1
    elif i == "4":
     counter4 = counter4 + 1
    elif i == "5":
     counter5 = counter5 + 1
    elif i == "6":
     counter6 = counter6 + 1
    else:
     counter7 = counter7 + 1

print(counter1)
print(counter2)
print(counter3)
print(counter4)
print(counter5)
print(counter6)
print(counter7)
