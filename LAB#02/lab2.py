# Create a parent class Array which takes one parameter to initialize: of an array. Use ctypes
# library to initialize size of array.

import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Size must be positive"
        self._size = size
        arraytype = ctypes.py_object * size
        self.elements = arraytype()
        self.clear(0)

    
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if index >= self._size:
            raise IndexError('Index out of range')
        return self.get_item(index)

    def __setitem__(self, index, value):
        if index >= self._size:
            raise IndexError('Index out of range')
        self.set_item(index, value)
    
    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value
        
    def __iter__(self):
        return _ArrayIterator(self.elements)

class _ArrayIterator:
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration

# A matrix is a collection of scalar values arranged in rows and columns as a rectangular grid of a fixed size.
# The elements of the matrix can be accessed by specifying a given row and column index with indices
# starting at 0

class Matrix:
    def __init__(self, rows, cols):
        assert rows > 0, "Number of rows must be positive"
        assert cols > 0, "Number of columns must be positive"
        self._rows = rows
        self._cols = cols
        arraytype = ctypes.py_object * (rows * cols)
        self.elements = arraytype()
        self.clear(0)
    
    def __len__(self):
        return self._rows
    
    def __getitem__(self, index):
        if index >= self._rows:
            raise IndexError('Index out of range')
        return self.get_item(index)
    
    def __setitem__(self, index, value):
        if index >= self._rows:
            raise IndexError('Index out of range')
        self.set_item(index, value)
    
    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value
    
    def get_item(self, row, col):
        assert row >= 0 and row < self._rows, "Row index out of range"
        assert col >= 0 and col < self._cols, "Column index out of range"
        return self.elements[row * self._cols + col]
    
    def set_item(self, row, col, value):
        assert row >= 0 and row < self._rows, "Row index out of range"
        assert col >= 0 and col < self._cols, "Column index out of range"
        self.elements[row * self._cols + col] = value
    
    def __iter__(self):
        return _MatrixIterator(self)

    def transpose(self):
        for row in range(self._rows):
            for col in range(self._cols):
                yield self.get_item(row, col)
        
    def scaleBy(self,scale):
        for row in range(self._rows):
            for col in range(self._cols):
                self.set_item(row, col, self.get_item(row, col) * scale)
            
    def add(self, other):
        assert self._cols == other._cols and self._rows == other._rows, "Matrices must have same dimensions"
        for row in range(self._rows):
            for col in range(self._cols):
                self.set_item(row, col, self.get_item(row, col) + other.get_item(row, col))
    
    def __str__(self):
        result = ""
        for row in range(self._rows):
            for col in range(self._cols):
                result += str(self.get_item(row, col)) + " "
            result += "\n"
        return result
    
    def sub(self, other):
        assert self._cols == other._cols and self._rows == other._rows, "Matrices must have same dimensions"
        for row in range(self._rows):
            for col in range(self._cols):
                self.set_item(row, col, self.get_item(row, col) - other.get_item(row, col))     

    def mul(self, other):
        assert self._cols == other._rows, "Number of columns in first matrix must equal number of rows in second matrix"
        result = Matrix(self._rows, other._cols)
        for row in range(self._rows):
            for col in range(other._cols):
                sum = 0
                for i in range(self._cols):
                    sum += self.get_item(row, i) * other.get_item(i, col)
                result.set_item(row, col, sum)
        return result

    def inverse(self):
        assert self._rows == self._cols, "Matrix must be square"
        result = Matrix(self._rows, self._cols)
        for row in range(self._rows):
            for col in range(self._cols):
                if row == col:
                    result.set_item(row, col, 1)
                else:
                    result.set_item(row, col, 0)
        for row in range(self._rows):
            for col in range(self._cols):
                if self.get_item(row, col) != 0:
                    result.set_item(row, col, 1 / self.get_item(row, col))
        return result

    

class _MatrixIterator:
    def __init__(self, the_matrix):
        self._matrix_ref = the_matrix
        self._cur_row = 0
        self._cur_col = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_row == self._matrix_ref._rows:
            raise StopIteration
        else:
            entry = self._matrix_ref.get_item(self._cur_row, self._cur_col)
            self._cur_col += 1
            if self._cur_col == self._matrix_ref._cols:
                self._cur_col = 0
                self._cur_row += 1
            return entry
    

obj = Matrix(3,3)
