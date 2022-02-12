#Task-1
class que:
    def __init__(self):
        self.qlist = list()
        
    def isenpty(self):
        return len(self.qlist) == 0
    
    def enque(self,item):
        self.qlist.append(item)
        
    def deque(self):
        assert not self.isenpty(), "Cannot remove item from empty lst"
        return self.qlist.pop()
    
    def show(self):
        print(self.qlist)
obj = que()

obj.enque(1)
obj.enque(2)
obj.enque(3)
obj.deque()
obj.show()

#Task-2
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
            
            
class ArrayQueue:
    def __init__(self, maxSize):
        self._count = 0 #count the number of item
        self._front = 0 #front set to 0 in the beginning
        self._back = maxSize - 1 #back at the end in the beginning
        self._qArray = Array(maxSize) #array to hold item

    #returns if the queue is empty
    def isEmpty(self):
        return self._count == 0

    #returns true if the queue is full
    def isFull(self):
        return self._count == len(self._qArray)

    #returns the no of itmes in the queue
    def __len__(self):
        return self._count

    #adds the given item to the queue
    def enqueue(self, item):
        assert not self.isFull(), "Queue filled up"
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1

    #removes and returns the first item
    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item
    
    def peek(self):
        assert not self.isEmpty(), "Queue is empty"
        return self._qArray[self._front]
    
    def traverse(self):
        for item in self._qArray:
            print(item)
            
            
obj = ArrayQueue(4)

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.traverse()    

#Task-3

class Queue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    #Returns true if the queue is empty
    def isEmpty(self):
        return self._qhead is None

    #Returns the number of items
    def __len__(self):
        return self._count

    #adds the given item to the queue
    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    #Removes and returns the first item
    def dequeue(self):
        assert not self.isEmpty(), "Can not be empty"
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item
    
    def traverse(self):
        assert not self.isEmpty()," cannot traverse through empty list"
        node = self._qhead
        
        while node:
            
            print(node.item)
            node = node.next

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        
        
obj = Queue()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)

obj.traverse()

#Task-4

class PriorityQueue:
    def __init__(self):
        """initlaizes a list for unbounded queue"""
        self._qList = list()

    def isEmpty(self):
        """True if queue is empty"""
        return len(self) == 0

    def __len__(self):
        return len(self._qList)
    #O(n) - but O(1) amortized cost
    def enqueue(self, item, priority):
        """New instance of storage class is created, and appended to the list"""
        entry = PriorityQEntry(item, priority)
        self._qList.append(entry)
    #O(n) as it transverses the list in worst possible case
    def dequeue(self):
        """Looks for the entry with highest priority and dequeue"""
        assert not self.isEmpty(), "Empty queue"
        index = 0
        highest = self._qList[index].priority
        for i in range(len(self)):
            if self._qList[i].priority < highest:
                highest = self._qList[i].priority
                index = i
        entry = self._qList.pop(index)
        return entry.item
    #__slots__ is good when many instances of the class is to be crated
    #the class should inherit object, and all of the inheritance shoulddelcare
    #__slot__ and not __dict__
    #arbirtray attributes can not be added in __slots__ unlike in __dict__ though
    def show(self):
        for i in self._qList:
            print("items, priority ",i.item,i.priority)
class PriorityQEntry(object):
        
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        
obj = PriorityQueue()       
obj.enqueue("student",3)
obj.enqueue("professor",2)
obj.enqueue("deen",1)
obj.dequeue()
obj.dequeue()
obj.show()

#Task-5
class PriorityLLQueue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        return self._qhead is None

    def _len_(self):
        return self._count

    def enqueue(self, item, priority):
        """Priority is the key for the queue"""
        node = _PriorityLLNode(item, priority)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1
    
    def dequeue(self):
        assert not self.isEmpty(), "Empty queue"
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item

    def peek(self):
        assert not self.isEmpty(), "Empty queue"
        return self._qhead.item
    
    def traverse(self):
        node = self._qhead
        while node is not None:
            print(node.item)
            node = node.next

class _PriorityLLNode(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None
        
obj = PriorityLLQueue()
obj.enqueue("student",1)
obj.enqueue("professor",2)
obj.dequeue()
obj.traverse()

#Task-6

class Queue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    #Returns true if the queue is empty
    def isEmpty(self):
        return self._qhead is None

    #Returns the number of items
    def __len__(self):
        return self._count

    #adds the given item to the queue
    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    #Removes and returns the first item
    def dequeue(self):
        assert not self.isEmpty(), "Can not be empty"
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item
    
    def traverse(self):
        assert not self.isEmpty()," cannot traverse through empty list"
        node = self._qhead
        
        while node:
            
            print(node.item)
            node = node.next

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None




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


class BPriority:
    def __init__(self,numLevel):
        self._qSize = 0
        self._qLevels = Array(numLevel)
        for i in range(numLevel):
            self._qLevels[i] = Queue()
        
    def isEmpty(self):
        return self._qSize == 0
    
    def __len__(self):
        return self._qSize
    
    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self._qLevels), "Invalid priority"

        q = self._qLevels[priority]
        q.enqueue(item)
        self._qSize += 1
    
    def dequeue(self):
        assert not self.isEmpty(), "Empty queue"
        for i in range(len(self._qLevels)):
            q = self._qLevels[i]
            if not q.isEmpty():
                self._qSize -= 1
                return q.dequeue()

    def peek(self):
        assert not self.isEmpty(), "Empty queue"
        for i in range(len(self._qLevels)):
            q = self._qLevels[i]
            if not q.isEmpty():
                return q.peek()
    def traverse(self):
        for i in range(len(self._qLevels)):
            q = self._qLevels[i]
            
            print("levels", i )
            q.traverse()
            


obj = BPriority(3)
obj.enqueue("A", 1)
obj.enqueue("B", 0)
obj.enqueue("C", 2)
obj.enqueue("D", 0)
obj.traverse()
print("Dequeue: ", obj.dequeue())

#Task-7

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue._count))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)