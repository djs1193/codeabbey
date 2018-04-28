def screensaver(h,w,wlength):
    q = -1
    x,y = 0,0
    vertical = 1
    horizontal = 1
    dims = [h,w]
    c = 0
    while q < 0 and c <= 100:
         print(x)
         print(y)
         print(" ")
         y += vertical
         x += horizontal
         if y == dims[0]-1:
             vertical = -1
         elif y == 0:
             vertical = 1
         if x == dims[1] - wlength:
             horizontal = -1
         elif x == 0:
             horizontal = 1
         c +=1

screensaver(19,42,5)
