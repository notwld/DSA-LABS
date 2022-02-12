#unsorted linear search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print("Linear search:", linear_search([25, 51, 72, 9, 10],10))	

#sorted linear search

def linear_search_sorted(theValues,item):
    n = len( theValues )
    for i in range ( n ) :
        if theValues [ i ] == item :
            return True
        elif theValues [ i ] > item :
            return False
    return False
print("Binary search:", linear_search_sorted([2, 5, 7, 9, 10],10))

#Binary search

def binary_search(theValues,item):
    first = 0
    last = len( theValues ) - 1
    found = False
    while ( first <= last and not found ):
        midpoint = ( first + last ) // 2
        if theValues [ midpoint ] == item :
            found = True
        else:
            if item < theValues [ midpoint ] :
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

print("Binary search:", binary_search([2, 5, 7, 9, 10], 5))

#Bubble sort

def bubble_sort(theValues):
    for passnum in range(len(theValues)-1,0,-1):
        for i in range(passnum):
            if theValues[i]>theValues[i+1]:
                temp = theValues[i]
                theValues[i] = theValues[i+1]
                theValues[i+1] = temp
    
    return theValues

print("Bubble sort:", bubble_sort([5,99,1,22,3,5,2,4,100]))

#Selection sort

def selection_sort(theValues):
    for fillslot in range(len(theValues)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if theValues[location]>theValues[positionOfMax]:
                positionOfMax = location
        temp = theValues[fillslot]
        theValues[fillslot] = theValues[positionOfMax]
        theValues[positionOfMax] = temp
    
    return theValues

print("Selection sort:", selection_sort([5,99,1,22,3,5,2,4,100]))

#Insertion sort

def insertion_sort(theValues):
    for index in range(1,len(theValues)):
        currentvalue = theValues[index]
        position = index
        while position>0 and theValues[position-1]>currentvalue:
            theValues[position]=theValues[position-1]
            position = position-1
        theValues[position]=currentvalue
    
    return theValues

print("Insertion sort:", insertion_sort([5,99,1,22,3,5,2,4,100]))

class Set:
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def __contains__(self,element):
        return element in self._list

    def add(self,element):
        assert element not in self._list, "Duplicate element"
        if element not in self._list:
            self._list.append(element)

    def remove(self,element):
        assert element not in self._list,"Element Dosenot exist ."
        if element in self._list:
            self._list.remove(element)

    def intersect(self,setB):
        newSet = Set()
        for i in range(len(self._list)):
            if setB[i] not in newSet._list and self._list[i] not in newSet._list:
                newSet._list.append(self._list[i])
        
        return newSet

    def union(self,setB):
        newSet = Set()
        for i in range(len(self._list)):
            if setB[i] not in newSet._list and self._list[i] not in newSet._list:
                newSet._list.append(self._list[i])
        
        return newSet
    
    def binary_search(self,item):
        first = 0
        last = len( self._list ) - 1
        found = False
        while ( first <= last and not found ):
            midpoint = ( first + last ) // 2
            if self._list[ midpoint ] == item :
                found = True
            else:
                if item < self._list [ midpoint ] :
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found

    

    def __iter__(self):
        return iter(self._list)

obj = Set()
obj.add(11)
obj.add(66)
obj.add(34)
obj.add(88)
obj.add(90)
obj.add(14)
print(obj.binary_search(88))


def findFirstOccurrence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid
            right = mid - 1
 
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
 
    return result


print("Modified binary search:", findFirstOccurrence([5,99,1,22,3,5,2,99,100],99))

def negative_values(theValues):
    for i in range(len(theValues)):
        if theValues[i] < 0:
            print(theValues[i], end = " ")
print("Negative values:")
negative_values([-5,0,5,6,-6,4,-3])

class Bag:
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def __contains__(self,element):
        return element in self._list

    def add(self,element):
        self._list.append(element)

    def remove(self,element):
        assert element in self._list,"Element Dosenot exist ."
        if element in self._list:
            self._list.remove(element)

    def __iter__(self):
        return iter(self._list)

    def binary_search(self,item):
        first = 0
        last = len( self._list ) - 1
        found = False
        while ( first <= last and not found ):
            midpoint = ( first + last ) // 2
            if self._list[ midpoint ] == item :
                found = True
            else:
                if item < self._list [ midpoint ] :
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found
    
obj2 = Bag()
obj2.add(11)
obj2.add(66)
obj2.add(34)
obj2.add(88)
obj2.add(90)
print(obj2.binary_search(90))

class Map:
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def __contains__(self,element):
        return element in self._list

    def add(self,element):
        self._list.append(element)

    def remove(self,element):
        assert element in self._list,"Element Dosenot exist ."
        if element in self._list:
            self._list.remove(element)

    def __iter__(self):
        return iter(self._list)

    def binary_search(self,key):
        first = 0
        last = len( self._list ) - 1
        found = False
        while ( first <= last and not found ):
            midpoint = ( first + last ) // 2
            if self._list[ midpoint ][0] == key :
                found = True
            else:
                if key < self._list [ midpoint ][0] :
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found


    def __getitem__(self,key):
        for i in range(len(self._list)):
            if self._list[i][0] == key:
                return self._list[i][1]
        return None
    
    def __setitem__(self,key,value):
        for i in range(len(self._list)):
            if self._list[i][0] == key:
                self._list[i][1] = value
                return
        self._list.append([key,value])

obj3 = Map()
obj3.add([11,22])
obj3.add([66,77])
obj3.add([34,55])
obj3.add([88,99])
print(obj3.binary_search(88))
