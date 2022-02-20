import ctypes

from numpy import array, identity, matrix

class Array:
    def __init__(self,size):
        self.size = size
        array = ctypes.py_object *size
        self.array = array()
        self.clear(0)

    def clear(self,clrw):
        for each in range(len(self.array)):
            self.array[each] = clrw

    def __len__(self):
        return self.size

    def __setitem__(self,index,item):
        self.array[index] = item

    def __getitem__(self,index):
        return self.array[index]

    def __iter__(self):
        return _ArrayItr(self.array)

class _ArrayItr:
    def __init__(self,array) -> None:
        self.array = array
        self.count = 0

    def __next__(self):
        if self.count<len(self.array):
            item = self.array[self.count]
            self.count+=1
            return item
        else:
            raise StopIteration()

    def __iter__(self):
        return self

# array = Array(5)
# array[0] = 5
# array[1] = 9
# array[2] = 4
# array[3] = 2
# array[4] = 8

# for each in range(len(array)):
#     print(array[each])

# print(array[0])

class Array2D:
    def __init__(self,rows,cols):
        self.array2d = Array(rows)
        for each in range(len(self.array2d)):
            self.array2d[each] = Array(cols)
        
    def __len__(self):
        return len(self.array2d)
    
    def numRows(self):
        return len(self.array2d)

    def numCols(self):
        return len(self.array2d[0])

    def __setitem__(self,ndxtuple,item):
        row = ndxtuple[0]
        col = ndxtuple[1]
        array = self.array2d[row]
        array[col] = item
    def __getitem__(self,ndxtuple):
        row = ndxtuple[0]
        col = ndxtuple[1]
        array = self.array2d[row]
        return array[col]

    def __iter__(self):
        return iter(self.array2d)

    def clear(self,clrw):
        for row in range(len(self.array2d)):
            self.array2d[row].clear(clrw)


class MultiArray:
    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "Dimensions can not be less than 1"
        self._dims = dimensions
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions should be greater than 0"
            size *= d
        #create a 1-D array to store all elements
        self._elements = Array(size)
        #create 1-D array to store the equation factors
        self._factors = Array(len(dimensions))
        self._computeFactors()
    #no of dimensions in the array
    def numDims(self):
        return len(self._dims)

    #returns the lenth of the given dimension
    def length(self, dim):
        assert dim >= 1 and dim <= len(self._dims),\
               "Dimension component out of range"
        return self._dims[dim-1]

    #def clears the array by setting all elements to value
    def clear(self, value):
        self._elements.clear(value)

    #returns the cotnest of element(i_1, i_2,..., i_n)
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid array subscripts!"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        return self._elements[index]

    #sets the contents of element(i_1, i_2, i_3,...i_n)
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        self._elements[index] = value

    #computes a 1-D array offset for element (i_1, i_2, ...i_n)
    #using the equation i_1 * f_1 + i_2 * f_2 +.... + i_n * f_n
    def _computeIndex(self, idx):
        offset = 0
        for j in range(len(idx)):
            #make sure the index componens within the legal range
            if idx[j] < 0 or idx[j] >= self._dims[j]:
                return None
            else:
                offset += idx[j] * self._factors[j]
        return offset

    #computes the factor values used in the index equation
    #done as part of exercise
    def _computeFactors(self):
        self._factors[len(self._factors)-1] = 1
        for j in reversed(range(len(self._factors) - 1)):
            self._factors[j] = self._factors[j+1] * self._dims[j+1]


# from random import randint
# multi = MultiArray(3,4,5)

# multi.clear(0)
# for i in range(multi.length(1)):
#     for j in range(multi.length(2)):
#         for k in range(multi.length(3)):
#             multi[i,j,k] = randint(1,100)

# for i in range(multi.length(1)):
#     for j in range(multi.length(2)):
#         for k in range(multi.length(3)):
#             print(multi[i,j,k], end = ' ')
#         print()

class ReportGenerator:
    def __init__(self, fileName):
        self._fileName = fileName
        self._inputFO = None #file object
        self._multiarray = MultiArray(5,20,12)

    def open(self):
        self._inputFO = open(self._fileName, "r")

    def close(self):
        self._inputFO.close()
        self._inputFO = None

    def load_data(self):
        self.open()
        for line in self._inputFO:
            words = line.split()
            if len(words) == 2:
                item_counter = 0
                f_index = int(words[1][1]) - 1#store index
            if len(words) == 13:
                if words[0] == "Item#":
                    pass
                else:
                    for i in range(12):
                        self._multiarray[f_index, item_counter, i] = float(words[i+1])
                    item_counter += 1
        self.close()
        return self._multiarray


rg = ReportGenerator('SaleData.txt') #creates the report generator object to read SalesData
salesData = rg.load_data() #returns the filled in multi array as SalesData
# Compute the total sales of all items for all months in a given store.
def totalSalesByStore( salesData, store ):
# Subtract 1 from the store # since the array indices are 1 less
# than the given store #.
    s = store-1
    # Accumulate the total sales for the given store.
    total = 0.0
    # Iterate over item.
    for i in range( salesData.length(2) ):
        # Iterate over each month of the i item.
        for m in range( salesData.length(3) ):
            total += salesData[s, i, m]
    return total

# Compute the total sales of all items in all stores for a given month.
def totalSalesByMonth( salesData, month ):
# The month number must be offset by 1.
    m = month - 1
    # Accumulate the total sales for the given month.
    total = 0.0
    # Iterate over each store.
    for s in range( salesData.length(1) ):
    # Iterate over each item of the s store.
        for i in range( salesData.length(2) ):
            total += salesData[s, i, m]
    return total

# Compute the total sales of a single item in all stores over all months.
def totalSalesByItem( salesData, item ):
# The item number must be offset by 1.
    i = item - 1
    # Accumulate the total sales for the given month.
    total = 0.0
    # Iterate over each store.
    for s in range( salesData.length(1) ):
    # Iterate over each month of the s store.
        for m in range( salesData.length(3) ):
            total += salesData[s, i, m]
    return total

# Compute the total sales per month for a given store. A 1-D array is
# returned that contains the totals for each month.
def totalSalesPerMonth( salesData, store ):
# The store number must be offset by 1.
    s = store - 1
    # The totals will be returned in a 1-D array.
    totals = Array( 12 )
    # Iterate over the sales of each month.
    for m in range( salesData.length(3) ):
        sum = 0.0
        # Iterate over the sales of each item sold during the m month.
        for i in range( salesData.length(2) ):
            sum += salesData[s, i, m]
        # Store the result in the corresponding month of the totals array.
        totals[m] = sum
    # Return the 1-D array.
    return totals
# print( totalSalesByStore(salesData,1) )#print stores 1 total sell
# print( totalSalesByItem(salesData, 2))#print items 2 total sell
# print( totalSalesByMonth(salesData, 4)) #print months April total sell
# salespermonth = totalSalesPerMonth(salesData, 1)#store1 total sell in each month
# for a in range(len(salespermonth)):
#     print( salespermonth[a])

#menu driven program    
def main():
    print("Welcome to the Sales Report Program")
    print("1. Total Sales by Store")
    print("2. Total Sales by Item")
    print("3. Total Sales by Month")
    print("4. Total Sales per Month")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            store = int(input("Enter store number: "))
            print("Total sales for store", store, "is", totalSalesByStore(salesData, store))
        elif choice == 2:
            item = int(input("Enter item number: "))
            print("Total sales for item", item, "is", totalSalesByItem(salesData, item))
        elif choice == 3:
            month = int(input("Enter month number: "))
            print("Total sales for month", month, "is", totalSalesByMonth(salesData, month))
        elif choice == 4:
            store = int(input("Enter store number: "))
            salespermonth = totalSalesPerMonth(salesData, store)
            for a in range(len(salespermonth)):
                print( salespermonth[a])
        else:
            print("Invalid choice")
        print("1. Total Sales by Store")
        print("2. Total Sales by Item")
        print("3. Total Sales by Month")
        print("4. Total Sales per Month")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
    print("Bye")

main()