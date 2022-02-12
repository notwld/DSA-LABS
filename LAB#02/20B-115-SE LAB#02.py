from PIL import Image
from statistics import mean
import ctypes

#LAB TASK # 1
class Array:
    def __init__(self,size):
        assert size >0, "Size must be positive"
        self.size = size
        arraytype = ctypes.py_object * size
        self.elements = arraytype()
        self.clear(0)

    def __len__(self):
        return self.size

    def __getitem__(self,i):
        assert i>=0 and i <len(self), "out of range"
        return self.elements[i]

    def __setitem__(self, i, value):
        assert i>=0 and i <len(self), "out of range"
        self.elements[i] = value

    def clear(self, value):
        for i in range(len(self.elements)):
            self.elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self.elements)

            
class _ArrayIterator:
    def __init__(self,array):
        self._arrayRef = array
        self._curr = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curr<len(self._arrayRef):
            element = self._arrayRef[self._curr]
            self._curr+=1
            return element
        else:
            raise StopIteration

#LAB TASK # 2
class Array2D:
    def __init__(self, numRows, numCols):
        self.rows = Array(numRows)
        for i in range(numRows):
            self.rows[i] = Array(numCols)
            
    def numRows(self):
        return len(self.rows)
        
    def numCols(self):
        return len(self.rows[0])
        
    def clear(self, value):
        for row in range(self.numRows()):
            self.rows[row].clear(value)
            
    def __getitem__(self, ndxTuple):
        assert len((ndxTuple)) == 2, "number of arrays is invalid"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row <self.numRows() and col >= 0 and col<self.numCols(), "Values out of range"
        array1d = self.rows[row]
        return array1d[col]
        
        
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "number of arrays is invalid"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row <self.numRows() and col >= 0 and col<self.numCols(), "Values out of range"
        array1d = self.rows[row]
        array1d[col] = value
    
    def __len__(self):
        return len(self.rows)

#LAB TASK # 3	
class Matrix:
    def __init__(self,rows,cols):
        assert rows>0,"Numbers of rows must be +ve"
        assert cols>0,"Numbers of cols must be +ve"
        self.mat=Array2D(rows,cols)

    def __len__(self):
        return len(self.mat)

    def __getItem__(self,ndxTuple):
        return self.mat[ndxTuple[0],ndxTuple[1]]
    
    def __setItem__(self,ndxTuple,scalerValue):
        self.mat[ndxTuple[0],ndxTuple[1]] = scalerValue

    def numRows(self):
        return self.mat.numRows()

    def numCol(self):
        return self.mat.numCols()

    def ScaleBy(self,scaler):
        self.mat
        



#Question 1

class GrayscaleImage:
    def __init__(self, imgFile):
        self._img = Image.open(imgFile, "r")
        self._width, self._height = self._img.size
        self._imgData = self._img.getdata()
        self._pixel_values = Array2D(self._width, self._height)
        
    def __str__(self):

        if self._img.mode == "RGB":
            channels = 3
            imgAvg = int(mean(self._imgData[0] + self._imgData[1] + self._imgData[2]))
        elif self._img.mode == "L":
            channels = 1
            imgAvg = self._imgData[0]
        else:
            print("Unknown mode: %s" % self._img.mode)
            return None

        return "Image Size {} x {} \n Image Data size {} \n channels {}".format(self._width,self._height,len(self._imgData),channels)


    def getImageData(self):
        counter = 0
        for i in range(self._width):
            j = 0
            while j <= 511:
                # print('({}x{})={}'.format(i,j,counter))
                self._pixel_values[i, j] = self._imgData[counter]
                j += 1
                counter += 1
        return self._pixel_values


    def imgWidth(self):
        return self._width

    def imgHeight(self):
        return self._height

    def clear(self, value):
        assert value>0 and value<256, "Value shoud be in range 0-255"
        for i in range(self._width):
            for j in range(self._height):
                self._pixel_values = value

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self._width \
            and col >= 0 and col < self._height,\
            "image width or Height out of range."
        return self._pixel_values[row,col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple)==2, "Invalid no of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >=0 and row < self._width \
            and col >= 0 and col < self._height, \
            "image width or Height out of range."
        self._pixel_values[row,col] = value

img1='pic1.jpeg'
img2='pic2.jpeg'
image2D=GrayscaleImage(img1)
imgdata=image2D.getImageData()
print(image2D)


#Question 2

class Matrix:
    def __init__(self,numRows,numCols):
        self.theGrid = Array2D(numRows,numCols)
        self.theGrid.clear(0)
    
    def numRows(self):
        return self.theGrid.numRows()
    
    def numCols(self):
        return self.theGrid.numCols()
    
    def __getitem__(self,ndxTuple):
        return  self.theGrid[ndxTuple[0],ndxTuple[1]]
    def __setitem__(self,ndxTuple,scalar):
        self.theGrid[ndxTuple[0],ndxTuple[1]] = scalar
    
    def scaleBy(self,scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r,c]*= scalar
                
                
                
    def __add__(self,rhsMatrix):
        assert rhsMatrix.numRows()==self.numRows() and rhsMatrix.numCols()== self.numCols(), "matrix seize not compatible"
        newMartix =Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMartix[r,c] = self[r,c]+ rhsMatrix[r,c]
        return newMartix
    
    def __sub__(self,rhsMatrix):
        assert rhsMatrix.numRows()==self.numRows() and rhsMatrix.numCols()== self.numCols(), "matrix seize not compatible"
        newMartix =Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMartix[r,c] = self[r,c]- rhsMatrix[r,c]
        return newMartix
    
    
    def transpose(self):

        newMatrix = Matrix(self.numCols(),self.numRows())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[c,r] = self[r,c]
        return newMatrix
    
    def __mul__(self, rhsMatrix):
        newMatrix = Matrix(self.numCols(),self.numRows())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                for v in range(rhsMatrix.numCols()):
                    newMatrix[r,v] += self[r,c] * rhsMatrix[c,v]
                    
        return newMatrix
    
    def inverseOfMatrix(self,AM,IM):
        for fd in range(len(AM)):
            fdScaler = 1.0 / AM[fd][fd]
        for j in range(len(AM)):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in list(range(len(AM)))[0:fd] + list(range(len(AM)))[fd+1:]:
            crScaler = AM[i][fd]
            for j in range(len(AM)):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
        return IM
    
obj = Matrix(2,2)
obj1 = Matrix(2,2)



obj1[0,0]=1
obj1[0,1]=0
obj1[1,0]=0
obj1[1,1]=1


obj[0,0]=2
obj[0,1]=6
obj[1,0]=1
obj[1,1]=4

trans = obj.transpose()

for i in range(obj.numRows()):
    print("")
    for j in range(obj.numCols()):
        print(obj[i,j],end="")

        
mlutiplication = obj*obj1

print("\n\nmatrix multiplication\n")      
for i in range(obj1.numRows()):
    print("")
    for j in range(obj1.numCols()):
        print(mlutiplication[i,j],end="")
        


#Question 3,4,5

class GameGrid:
    deadcell = 0
    livecell = 1
    def __init__(self,numrows,numcols):
        self.grid = Array2D(numrows,numcols)
        self.configure(list())
    def numofrow(self):
        return self.grid.numRows()
    def numofcol(self):
        return self.grid.numCols()
    
    def configure(self,coordlist):
        for i in range(self.numofrow()):
            for j in range(self.numofcol()):
                self.clear(i,j)
                
        for coord in coordlist:
            self.setCellLive(coord[0],coord[1])

    def setCellLive(self,row,col):
        self.grid[row,col] = GameGrid.livecell
                
    def clear(self,r,c):
        self.grid[r,c] = GameGrid.deadcell
    def isLiveCell(self,row,col):
        return self.grid[row,col] == GameGrid.livecell
    def isDeadCell(self,row,col):
        return self.grid[row,col] == GameGrid.deadcell
    
    def numofLiveNeighbours(self,r,c):
        count =0
        
        o = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        
        for i in o:
            x = i[0] + r
            y = i[1] + c
            
            if x>= 0 and x <self.numofrow() and y>=0 and y<self.numofcol() and self.grid[x,y]==1:
                count +=1
            
            
        
        return count

    def evolve(self):
        newgrid = Array2D(self.numofrow(),self.numofcol())
        
        livecells = list()
        
        for i in range(self.numofrow()):
            for j in range(self.numofcol()):
                neighbors = self.numofLiveNeighbours(i,j)
                
                if (neighbors ==2 and self.isLiveCell(i,j)) or neighbors == 3:
                    livecells.append((i,j))
        self.configure(livecells)
        
            
    
    def draw(self):
        for r in range(self.numofrow()):
            print("")
            for c in range(self.numofcol()):
                print(" . ",end="@")
                # self.grid[r,c]
                
rowIn = int(input("Enter the number of rows : "))
colIn = int(input("Enter the number of columns : "))
obj = GameGrid(rowIn,colIn)
obj.configure([(1,1),(1,2),(1,3)])
obj.evolve()
obj.draw()


             
