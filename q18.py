# calculating the check sum

list1 = [
74, 270, 7 ,27 ,30, 6281640, 71709, 23, 7821, 4491167, 759, 5377, 10, 47660, 505998, 7157, 605, 243904984, 197, 49734, 22678, 15, 295, 6499, 1 ,4 ,54048873 ,987748185, 47933]




def checksum(alist):
    res = 0
    for i in alist :
        res = res + i
        res = (res*113)%10000007
    print(res)


checksum(list1)
