import math


mylist = [
'go 200 feet by azimuth 315',
'go 160 feet by azimuth 22',
'go 40 feet by azimuth 356',
'go 100 feet by azimuth 54',
'go 120 feet by azimuth 75',
'go 380 feet by azimuth 39',
'go 440 feet by azimuth 276',
'go 340 feet by azimuth 323',
'go 480 feet by azimuth 15',
'go 20 feet by azimuth 314',
'go 140 feet by azimuth 66',
'go 140 feet by azimuth 83',
'go 80 feet by azimuth 316',
'go 240 feet by azimuth 334',
'go 60 feet by azimuth 58',
'go 40 feet by azimuth 329',
'go 480 feet by azimuth 351'
]
distance_list = []
azimuth_list =[]
for i in mylist:
    distance_list.append(int(i[3:6]))
for i in mylist:
    azimuth_list.append((math.radians(int(i[-3:]))))



starting_pos_x = 0
starting_pos_y = 0

for i in range(0,len(distance_list)):
    starting_pos_x +=  (math.sin(azimuth_list[i])*distance_list[i])
    starting_pos_y +=  (math.cos(azimuth_list[i])*distance_list[i])

print(round(starting_pos_x))
print(round(starting_pos_y))
