# double dice role

def doubledice(role1,role2):
    r1 = role1%6 +1
    r2 = role2%6 +1
    res = r1 +r2
    print(res)
    print(" ")

list1 = [
[1481155651 ,94262043],
[1870105772 ,1971280765],
[667221736 ,88546897],
[1896731214 ,1474760247],
[1175797578 ,977425202],
[1901448133 ,1622381724],
[550840488 ,604854535],
[373710231 ,1223366348],
[1612622280 ,187782015],
[2025341675 ,2015544923],
[281891121 ,449971015],
[1809921499 ,729186200],
[326393631 ,893923171],
[265221197 ,123242296],
[1404581881 ,87208029],
[1739730833 ,1488639733],
[122476554 ,791403953],
[1922239180 ,9319592],
[993317260 ,849758148],
[1186808281 ,185127348],
[596276360 ,368546689],
[1255138429 ,1912713862],
[466462397 ,301252773],
[441729566 ,736865527]
]

for i in list1:
    doubledice(i[0],i[1])
