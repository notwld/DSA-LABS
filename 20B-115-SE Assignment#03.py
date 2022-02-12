def board():
    li = []
    for i in range(3):
        li.append([0]*3)
    return li


def rec(board,player,row,col):
    if row == 3 or col == 3:
        return True
    else:
        if board[row][col] == 0:
            board[row][col] = player
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            if rec(board,player,row,col+1) or rec(board,player,row+1,col):
                return True
            else:
                board[row][col] = ''
                return False
        else:
            return rec(board,player,row+1,col)

check = board()
print(rec(check,'X',0,0))
for i in check:
    print(i)
print(rec(check,'X',0,1))
for i in check:
    print(i)
print(rec(check,'X',1,0))
for i in check:
    print(i)
print(rec(check,'X',1,1))
for i in check:
    print(i)
print(rec(check,'O',0,0))
for i in check:
    print(i)
print(rec(check,'O',0,1))
for i in check:
    print(i)
print(rec(check,'O',1,0))
for i in check:
    print(i)
print(rec(check,'O',1,1))
for i in check:
    print(i)