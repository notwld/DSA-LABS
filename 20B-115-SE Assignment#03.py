# def board():
#     li = []
#     for i in range(3):
#         li.append([0]*3)
#     return li


# def rec(board,player,row,col):
#     if row == 3 or col == 3:
#         return True
#     else:
#         if board[row][col] == 0:
#             board[row][col] = player
#             if player == 'X':
#                 player = 'O'
#             else:
#                 player = 'X'
#             if rec(board,player,row,col+1) or rec(board,player,row+1,col):
#                 return True
#             else:
#                 board[row][col] = ''
#                 return False
#         else:
#             return rec(board,player,row+1,col)

# check = board()
# print(rec(check,'X',0,0))
# for i in check:
#     print(i)
# print(rec(check,'X',0,1))
# for i in check:
#     print(i)
# print(rec(check,'X',1,0))
# for i in check:
#     print(i)
# print(rec(check,'X',1,1))
# for i in check:
#     print(i)
# print(rec(check,'O',0,0))
# for i in check:
#     print(i)
# print(rec(check,'O',0,1))
# for i in check:
#     print(i)
# print(rec(check,'O',1,0))
# for i in check:
#     print(i)
# print(rec(check,'O',1,1))
# for i in check:
#     print(i)

import random
from ADTs import Array2D

class TicTacToe:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.board = Array2D(row,col)
        for i,j in range(row,col):
            self.board[i,j] = Array2D(row,col)
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

obj = TicTacToe(3,3)