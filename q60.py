

def tictac(list1):
    board = [1,2,3,4,5,6,7,8,9]
    list2 = list1.split()
    count = 0
    end = False
    for i in list2:
        p = int(i)-1
        if count%2 == 0:
            board[p] = "X"
        else:
            board[p] = "O"
        if ((board[0] == board[1] == board[2] == 'X') or (board[3] == board[4]== board[5] == 'X') or (board[6] == board[7] == board[8] == 'X') or
        (board[0] == board[4] == board[8] == 'X') or (board[2] == board[4] == board[6] == 'X')
        or (board[0] == board[3] == board[6] == 'X') or (board[1] == board[4] == board[7] == 'X') or (board[2] == board[5] == board[8] == 'X')):
            print(count+1)
            print(" ")
            end = True
            break
        if ((board[0] == board[1] == board[2] == 'O') or (board[3] == board[4]== board[5] == 'O') or (board[6] == board[7] == board[8] == 'O') or
        (board[0] == board[4] == board[8] == 'O') or (board[2] == board[4] == board[6] == 'O')
        or (board[0] == board[3] == board[6] == 'O') or (board[1] == board[4] == board[7] == 'O') or (board[2] == board[5] == board[8] == 'O')):
            print(count+1)
            print(" ")
            end = True
            break
        count += 1
        if count == 9 and end == False:
              print(0)
              print(" ")

mystr = [
'1 6 5 7 2 3 4 8 9',
'3 2 9 1 6 4 7 8 5',
'4 9 3 2 5 6 7 1 8',
'7 1 3 8 2 9 4 5 6',
'1 3 6 5 2 8 7 9 4',
'1 2 8 9 7 6 4 5 3',
'5 8 3 2 1 9 4 6 7',
'5 1 6 2 7 8 4 3 9',
'4 3 1 6 7 2 8 5 9',
'5 3 7 9 2 4 1 6 8',
'8 3 7 2 1 4 9 6 5'
 ]
for i in mystr:
    tictac(i)
