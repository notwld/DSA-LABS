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

import random
import ctypes
class Array:
    def __init__(self,size):
        assert size > 0
        self.size = size
        PyArraytype = ctypes.py_object * size
        self.element = PyArraytype()
        self.clear(2)
    def __len__(self):
        return self.size
    def __getitem__(self, index):
        assert index >=0 and index < len(self)
        return self.element[index]
    def __set__(self, index, value):
        assert index >=0 and index < len(self)
        self.element[index] = value
    def clear(self,value):
        for i in range(len(self)):
            self.element[i]=value

class Array2d:
    def __init__(self,numRows, numCols):
        self.row = numRows
        self.column = numCols
        self.rows = Array(numRows)
        for i in range(numRows):
            self.rows.element[i] = Array(numCols)

    def numRows(self):
        return len(self.rows)
    def numCols(self):
        return len(self.rows[0])
    def __setitem__(self, i,j, value):
        assert i >= 0 and i < len(self.rows) and j >= 0 and j < len(self.rows[0]), "Values out of range"
        array1d = self.rows[i]
        array1d.element[j] = value

    def __getitem__(self, i,j):
        assert i >= 0 and i < len(self.rows) and j >= 0 and j < len(self.rows[0]),"Values out of range"
        array1d = self.rows[i][j]
        return array1d

class TicTacToe:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.board = Array2d(row,col)
        for i,j in range(row,col):
            self.board[i,j] = Array2d(row,col)
        self.clear(".")
        self.movebyhuman()
    def clear(self,st):
        for i in range(self.row):
            for j in range(self.col):
                self.board.__setitem__(i,j,st)
        for i in range(self.row):
            print(" ")
            for j in range(self.col):
                print(self.board.__getitem__(i,j),end=" | ")

    def movebycomputer(self):
        print()
        num = random.randint(1,9)
        if num == 1 and self.board.__getitem__(0,0) == "." and self.board.__getitem__(0,0) != "0":
            print("Move of computer on ",num,"position")
            self.board.__setitem__(0,0,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 2 and self.board.__getitem__(0,1) == "." and self.board.__getitem__(0,1) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(0,1,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 3 and self.board.__getitem__(0,2) == "."and self.board.__getitem__(0,2) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(0,2,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 4 and self.board.__getitem__(1,0) == "." and self.board.__getitem__(1,0) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(1,0,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 5 and self.board.__getitem__(1,1) == "." and self.board.__getitem__(1,1) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(1,1,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 6 and self.board.__getitem__(1,2) == "." and self.board.__getitem__(1,2) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(1,2,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 7 and self.board.__getitem__(2,0) == "." and self.board.__getitem__(2,0) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(2,0,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 8 and self.board.__getitem__(2,1) == "." and self.board.__getitem__(2,1) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(2,1,"X")
            self.print_board()
            self.computer_winner_horizontal()
        elif num == 9 and self.board.__getitem__(2,2) == "." and self.board.__getitem__(2,2) != "0":
            print("Move of computer on ", num, "position")
            self.board.__setitem__(2,2,"X")
            self.print_board()
            self.computer_winner_horizontal()
        else:
            self.movebycomputer()

    def movebyhuman(self):
        print()
        num1 = int(input("Enter your move from (1,9): "))
        if num1 == 1 and self.board.__getitem__(0,0) == "." and self.board.__getitem__(0,0) != "X":
            self.board.__setitem__(0,0,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 2 and self.board.__getitem__(0,1) == "." and self.board.__getitem__(0,1) != "X":
            self.board.__setitem__(0,1,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 3 and self.board.__getitem__(0,2) == "."and self.board.__getitem__(0,2) != "X":
            self.board.__setitem__(0,2,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 4 and self.board.__getitem__(1,0) == "." and self.board.__getitem__(1,0) != "X":
            self.board.__setitem__(1,0,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 5 and self.board.__getitem__(1,1) == "." and self.board.__getitem__(1,1) != "X":
            self.board.__setitem__(1,1,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 6 and self.board.__getitem__(1,2) == "." and self.board.__getitem__(1,2) != "X":
            self.board.__setitem__(1,2,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 7 and self.board.__getitem__(2,0) == "." and self.board.__getitem__(2,0) != "X":
            self.board.__setitem__(2,0,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 8 and self.board.__getitem__(2,1) == "." and self.board.__getitem__(2,1) != "X":
            self.board.__setitem__(2,1,"0")
            self.print_board()
            self.human_winner_horizontal()
        elif num1 == 9 and self.board.__getitem__(2,2) == "." and self.board.__getitem__(2,2) != "X":
            self.board.__setitem__(2,2,"0")
            self.print_board()
            self.human_winner_horizontal()
        else:
            print("check your move if it is repeated or out of given range (1-9)")
            self.movebyhuman()

    def human_winner_horizontal(self):
        if self.board.__getitem__(0,0) == "0" and self.board.__getitem__(0,1) == "0" and self.board.__getitem__(0,2) == "0":
            print("you win")
            return
        elif self.board.__getitem__(1,0) == "0" and self.board.__getitem__(1,1) == "0" and self.board.__getitem__(1,2) == "0":
            print("you win")
            return
        elif self.board.__getitem__(2,0) == "0" and self.board.__getitem__(2,1) == "0" and self.board.__getitem__(2,2) == "0":
            print("you win")
            return
        else:
            self.human_winner_vertical()
    def human_winner_vertical(self):
        if self.board.__getitem__(0,0) == "0" and self.board.__getitem__(1,0) == "0" and self.board.__getitem__(2,0) == "0":
            print("you win")
            return
        elif self.board.__getitem__(0,1) == "0" and self.board.__getitem__(1,1) == "0" and self.board.__getitem__(2,1) == "0":
            print("you win")
            return
        elif self.board.__getitem__(0,2) == "0" and self.board.__getitem__(1,2) == "0" and self.board.__getitem__(2,2) == "0":
            print("you win")
            return
        else:
            self.human_winner_diagonal()

    def human_winner_diagonal(self):
        if self.board.__getitem__(0,0) == "0" and self.board.__getitem__(1,1) == "0" and self.board.__getitem__(2,2) == "0":
            print("you win")
            return
        else:
            self.movebycomputer()

    def computer_winner_horizontal(self):
        if self.board.__getitem__(0, 0) == "X" and self.board.__getitem__(0, 1) == "X" and self.board.__getitem__(0,2) == "X":
            print("computer win")
            return
        elif self.board.__getitem__(1, 0) == "X" and self.board.__getitem__(1, 1) == "X" and self.board.__getitem__(1,2) == "X":
            print("computer win")
            return
        elif self.board.__getitem__(2, 0) == "X" and self.board.__getitem__(2, 1) == "X" and self.board.__getitem__(2,2) == "X":
            print("computer win")
            return
        else:
            self.computer_winner_vertical()

    def computer_winner_vertical(self):
        if self.board.__getitem__(0, 0) == "X" and self.board.__getitem__(1, 0) == "X" and self.board.__getitem__(2,0) == "X":
            print("computer win")
            return
        elif self.board.__getitem__(0, 1) == "X" and self.board.__getitem__(1, 1) == "X" and self.board.__getitem__(2,1) == "X":
            print("computer win")
            return
        elif self.board.__getitem__(0, 2) == "X" and self.board.__getitem__(1, 2) == "X" and self.board.__getitem__(2,2) == "X":
            print("computer win")
            return
        else:
            self.computer_winner_diagonal()

    def computer_winner_diagonal(self):
        if self.board.__getitem__(0, 0) == "X" and self.board.__getitem__(1, 1) == "X" and self.board.__getitem__(2,2) == "X":
            print("computer win")
            return
        else:
            self.movebyhuman()

    def print_board(self):
        for i in range(self.row):
            print(" ")
            for j in range(self.col):
                print(self.board.__getitem__(i,j),end=" | ")

# obj = TicTacToe(3,3)

def conflict(board):
    n = len(board)

    row_frequency = [0] * n
    main_diag_frequency = [0] * (2 * n)
    secondary_diag_frequency = [0] * (2 * n)

    for i in range(n):
        row_frequency[board[i]] += 1
        main_diag_frequency[board[i] + i] += 1
        secondary_diag_frequency[n - board[i] + i] += 1

    # print(row_frequency)
    # print(main_diag_frequency)
    # print(secondary_diag_frequency)

    conflicts = 0
    # formula: (N * (N - 1)) / 2
    for i in range(2*n):
        if i < n:
            conflicts += (row_frequency[i] * (row_frequency[i]-1)) / 2
        conflicts += (main_diag_frequency[i] * (main_diag_frequency[i]-1)) / 2
        conflicts += (secondary_diag_frequency[i]
                      * (secondary_diag_frequency[i]-1)) / 2
    return int(conflicts)


# test board
# 0 - indexed row / column values
board = [2, 3, 2, 1]
conflicts = conflict(board)
print(conflicts)