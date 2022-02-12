# stack ADT using linked list

from math import sin,cos,tan,sqrt
import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        #create the array structure using the ctypes module
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        #initialize each element using clear method of Array class
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >=0 and index < len(self), "Array subscript out of range!"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >=0 and index < len(self), "Array subscript out of range!"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple)==2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(),\
            "Array subscript out of range"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple)==2, "Invalid no of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >=0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value
class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def peek(self):
        assert not self.isEmpty(), "Empty stack"
        return self._top.item
    def pop(self):
        assert not self.isEmpty(), "Empty stack"
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1

class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())



def  infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack ()
    postfixList = []
    tokenList = infixexpr.split ()
    print("Token  List: ",tokenList)
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
            print('postfixList: ', postfixList)
        elif token == '(':
            opStack.push(token)
            print('Taken is (, push  into  opStack: ', opStack.peek())
        elif token == ')':
            print('Taken is ), pop opStack: ')
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            if opStack.isEmpty() == True:
                opStack.push(token)
            elif opStack.isEmpty() == False:
                if (prec[opStack.peek()] >= prec[token]):
                    print('opStack peek % c >= token % c, put % c in thepostfixList: ' % (opStack.peek(), token, opStack.peek()))
                    postfixList.append(opStack.pop())
                    opStack.push(token)
                    print('token is % c, push into opStack: ' % (token))
                elif (prec[opStack.peek()] <= prec[token]):
                    opStack.push(token)
    while not opStack.isEmpty():
        print('Stack Peek put into postfixList: ', opStack.peek())
        postfixList.append(opStack.pop())
    return "Postfix is"," ".join(postfixList)
obj = infixToPostfix("A + B * C / ( E - F )")
print(obj)

def  evaluatePostfix(e):
    size = len(e)
    a = 0
    b= 0
    s = Stack ()
    isVaild = True
    i = 0
    # work  with (+,-,/,*,%)  operator
    while (i < size  and  isVaild):
        if (e[i]  >= '0'and e[i]  <= '9'):
            # a = ord(e[i]) - ord('0')
            s.push(int(e[i]))
        elif (len(s) > 1):
            print(s.peek())
            a = s.pop()
            b = s.pop()
            #   Perform  arithmetic  operations  between 2 operands
            if (e[i] == '+'):
                s.push(b + a)
            elif (e[i] == '-'):
                s.push(b - a)
            elif (e[i] == '*'):
                s.push(b * a)
            elif (e[i] == '/'):
                s.push(int(b / a))
            elif (e[i] == '%'):
                s.push(b % a)
            else: #   When  use  other  operator
                isVaild = False
        elif (len(s) == 1):
            if (e[i] == '-'):
                a = s.pop()
                s.push(-a)
            elif (e[i] != '+'):#   When  not  use   +,-
                 isVaild = False
            else:
                isVaild = False
        if (isVaild  ==  False):#   Possible  case  use  other  operators#   1) When  using  special  operators#   2) Or  expression  is  invalid
             print(e, " Invalid  expression ")
             return
        i += 1
    if s._len_() == 1:
        return s.peek()
    else:
        return "error"
obj1 = evaluatePostfix("82*+3/")
print(obj1)


# implementation of task 2
class PostfixCalculator:
    def __init__(self):
        self.operandStack = Stack()
        self.saveStack = Stack()

    def value(self,x):
        #Pushes the given operand x onto the top of the stack.
        self.operandStack.push(x)
    def result(self):
        # Returns an alias to the value currently on top of the stack. If the stack is empty,None is returned
        assert not self.operandStack.isEmpty(), "Empty stack"
        return self.operandStack.peek()
    def clear(self):
        # Removes all elements from the stack.
        for i in range(len(self.operandStack)):
            self.operandStack.pop()
        for i in range(len(self.saveStack)):
            self.saveStack.pop()
    def clearLast(self):
        # Removes the top entry from the stack and discards it
        assert not self.operandStack.isEmpty(), "Empty stack"
        self.operandStack.pop()
    def compute( self,op ): 
#         Removes the top two values from the stack and applies the given operation
# on those values. The first value removed from the stack is the righthand side operand and the
# second is the lefthand side operand. The result of the operation is pushed back onto the stack.
# The operation is specified as a string containing one of the operators + - * / **.

        assert not self.operandStack.isEmpty(), "Empty stack"
        assert len(self.operandStack) >= 2, "Not enough operands"
        b = self.operandStack.pop()
        a = self.operandStack.pop()
        if op == "+":
            self.operandStack.push(a + b)
        elif op == "-":
            self.operandStack.push(a - b)
        elif op == "*":
            self.operandStack.push(a * b)
        elif op == "/":
            self.operandStack.push(a / b)
        elif op == "**":
            self.operandStack.push(a ** b)
        elif op=='abs':
            self.operandStack.push(abs(a))
        elif op=='sqrt':
            self.operandStack.push(sqrt(a))
        elif op=='sin':
            self.operandStack.push(sin(a))
        elif op=='cos':
            self.operandStack.push(cos(a))
        elif op=='tan':
            self.operandStack.push(tan(a))
        else:
            assert False, "Invalid operation"

    def store(self):
        # Removes the top value from the operand stack and pushes it onto the save stack.
        assert not self.operandStack.isEmpty(), "Empty stack"
        self.saveStack.push(self.operandStack.pop())
    def recall(self):
        #Removes the top value from the save stack and pushes it onto the operand stack.
        assert not self.saveStack.isEmpty(), "Empty stack"
        self.operandStack.push(self.saveStack.pop())

#test the postfix calculator
calc = PostfixCalculator()
calc.value(2)
calc.value(3)
calc.compute("+")
print(calc.result())
calc.value(4)
calc.compute("*")
print(calc.result())
calc.value(2)
calc.value(5)
calc.compute("**")
print(calc.result())

        

# Task 3
# Implement a complete maze solving application using the components introduced earlier in the chapter. Modify the solve() method to return a vector containing tuples representing the path through
# the maze.



class Maze:
    #Define constants to represent cell content
    MAZE_WALL = '@'
    PATH_TOKEN = 'X'
    TRIED_TOKEN = 'o'

    #Creates a maze object
    def __init__(self, numRows, numCols):
        self._mazeCells = Array2D(numRows, numCols)
        self._startCell = None
        self._exitCell = None

    #Returns the number of rows
    def numRows(self):
        return self._mazeCells.numRows()

    #Returns the number of columns
    def numCols(self):
        return self._mazeCells.numCols()

    #Fills the indicated cell with a wall marker
    def setWall(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell index out of range"
        self._mazeCells[row, col] = self.MAZE_WALL


    #sets the starting cell position
    def setStart(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell index out of range"
        self._startCell = _CellPosition(row, col)

    #sets the exit cell position
    def setExit(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell index out of range"
        self._exitCell = _CellPosition(row, col)

    #attempts to solve the maze by finding path from start to exit
    #returns True if found, otherwise False
    #stack contains the _CellPosition items,
    def findPath(self):
        s = Stack()#stack to save the path
        s.push(self._startCell)
        self._markPath(self._startCell.row, self._startCell.col)
        while True:
            #inside the loop where neighbor cell is checked for valid move
            #same time, checked if we get the exit
            if s.isEmpty():
                return False
            current_cell = s.peek()
            row = current_cell.row
            col = current_cell.col
            if not self._exitFound(row, col):
                for r in [row-1, row, row+1]:
                    if not (current_cell.row == s.peek().row and \
                            current_cell.col == s.peek().col):
                        break
                    for c in [col-1, col, col+1]:
                        if ((r == row) ^ (c == col)):
                            if self._validMove(r,c):
                                self._markPath(r,c)
                                s.push(_CellPosition(r,c))
                                break
                if current_cell.row == s.peek().row and\
                        current_cell.col == s.peek().col:
                    not_in_path = s.pop()
                    self._markTried(not_in_path.row, not_in_path.col)

            else:
                return True

    #Resets the maze by removing all "path" and "tried" tokens
    def reset(self):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                if self._mazeCells[r,c] == self.PATH_TOKEN or \
                        self._mazeCells[r,c] == self.TRIED_TOKEN:
                    self._mazeCells.clear()

    #prints a text represenation of the maze
    def draw(self):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                if self._mazeCells[r,c] is not None:
                    print(self._mazeCells[r,c], sep = ' ', end= ' ')
                else:
                    if self._startCell.row == r and self._startCell.col == c:
                        print('s', sep = ' ', end = ' ')
                    elif self._exitCell.row == r and self._exitCell.col == c:
                         print('e', sep = ' ', end = ' ')
                    else:
                        print('.', sep = ' ', end = ' ')
            print ('\n')
        print ("--------------------------")

    #Returns True if the given cell position is a valid move
    def _validMove(self, row, col):
        return row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols()\
            and self._mazeCells[row, col] is None

    #Helper method to find if exit was found
    def _exitFound(self, row, col):
        return row == self._exitCell.row and \
            col == self._exitCell.col

    #Drops a "tried" token at the given cell
    def _markTried(self, row, col):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    #Drops a "path" token at the given cell
    def _markPath(self, row, col):
        self._mazeCells[row, col] =self.PATH_TOKEN

#Private storage class for holding a cell position
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

def main():
    maze = buildMaze("mazefile.txt")
    print("Maze in the beginning")
    maze.draw()
    if maze.findPath():
        print("Path found...")
        maze.draw()
    else:
        print ("Path not found")

#build maze based on the configuration file
def buildMaze(filename):
    infile = open(filename, "r")
    #read rows and columns
    nrows, ncols = readValuePair(infile)
    maze = Maze(nrows, ncols)
    #read the starting and exit pos
    row, col = readValuePair(infile)
    maze.setStart(row,col)
    row, col = readValuePair(infile)
    maze.setExit(row, col)

    #constructs the maze from config file
    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            if line[col] == '@':
                maze.setWall(row, col)
    #close the maze file
    infile.close()
    return maze

#extracts an integer value pair from the given input file
def readValuePair(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)

#execute main routine
main()