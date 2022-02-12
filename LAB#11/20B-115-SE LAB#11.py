# Task 1
def rec(stri,n):
    if n > 0:
        rec(stri,n-1)
        if stri[n-1] != stri[len(stri)-n]:
            return False
    return True

words = "abcdcba"

print(rec(words,len(words)-1))

# Task 2
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(112,60))


# Task 3
def pascal_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        prev = pascal_triangle(n-1)
        curr = [1]
        for i in range(len(prev[-1])-1):
            curr.append(prev[-1][i]+prev[-1][i+1])
        curr.append(1)
        prev.append(curr)
        return prev

for i in pascal_triangle(5):
    print(i)


# Task 4
def board():
    return [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]


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