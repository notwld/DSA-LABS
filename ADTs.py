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
        

