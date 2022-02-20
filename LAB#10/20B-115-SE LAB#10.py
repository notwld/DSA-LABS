#TASK 1
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class linked:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,data):
        newnode = Node(data)
        
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            
        elif data < self.head.data:
            newnode.next = self.head
            self.head.prev = newnode
            
            self.head = newnode
        elif data > self.tail.data:
            
            self.tail.next = newnode
            newnode.prev = self.tail
            
            self.tail = newnode
            
        else:
            
            node = self.head
            
            while node and data > node.data:
                node = node.next
                
            if node == None:
                return False
            else:
                
                newnode.next = node
                node.prev.next = newnode
                newnode.prev = node.prev
                node.prev = newnode
                
    def insertatStrat(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode

        else:
            #temp = self.head

            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            
    def insertatEnd(self,data):
        newnode = Node(data)
        if self.tail == None:
            self.head = newnode
            self.tail = newnode

        else:
            #temp = self.head

            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode 
            
            

    def traverse(self):
        node= self.head
        
        while node:
            print(node.data)
            
            node = node.next
            
    def traverseReverse(self):
        node= self.tail
        
        while node:
            print(node.data)
            
            node = node.prev
            
    def remove(self,data):
        
        if data == self.head.data:
            self.head = self.head.next
            self.head.prev = None
        elif data == self.tail.data:
            self.tail = self.tail.prev
            
            self.tail.next = None
            
        else:
            
            node = self.head
            
            while node and node.data != data:
                node = node.next
                
            if node == None:
                return False
            else:
                node.prev.next = node.next
                node.next.prev = node.prev 
                
print("\n\n Task 1 \n\n")            
obj = linked()
obj.insert(4)
obj.insert(2)
obj.insert(1)
obj.insert(0)
obj.insert(6)
obj.insert(3)
obj.insert(5)
obj.insertatEnd(-1)
obj.remove(3)
obj.traverse()
print("-----------------------------")
obj.traverseReverse()

#TASK 02
class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
            
        else:
            self.tail.next = newNode
            
            self.tail = newNode
            newNode.next = self.head
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            
            self.tail.next = self.head
            self.size -= 1
            return data

    def printQueue(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    return 
            print()

    def __len__(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def first(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def rotate(self):
        if self.head is None:
            return
        else:
            self.tail = self.tail.next
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail

print("\nCircular Queue")
cirQ = CircularQueue()
cirQ.enqueue(10)
cirQ.enqueue(20)
cirQ.enqueue(30)
cirQ.enqueue(40)
cirQ.printQueue()


cirQ.rotate()
print("\n\n")
cirQ.printQueue()

class DblCircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
            newNode.prev = self.tail
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            newNode.next = self.head
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size -= 1
            return data

    def printQueue(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()

    def __len__(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def first(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def rotate(self):
        if self.head is None:
            return
        else:
            self.tail = self.tail.next
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail

print("\n\n\nDbl Circular Queue")
dblCirQ = DblCircularQueue()
dblCirQ.enqueue(10)
dblCirQ.enqueue(20)
dblCirQ.enqueue(30)
dblCirQ.enqueue(40)
dblCirQ.printQueue()
print(len(dblCirQ))
print(dblCirQ.isEmpty())
print(dblCirQ.first())
dblCirQ.rotate()
print(" ")
dblCirQ.printQueue()

# TASK 03
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None
class multiLevelNode():
    def __init__(self):
            self._head=None
            self._size=0
    def traverseNext(self, Node,data):
        nextlink = None
        curNode = Node
        while (curNode != None):
            if curNode.data==data:
                return nextlink , True
            nextlink = curNode
            curNode = curNode.next
        return nextlink, False
    def traverseChild(self, Node):
        curNode = Node
        while (curNode != None):
            nextchild = curNode
            curNode = curNode.child
        return nextchild

    def createNode(self, data):


        duplicate = False
        if self._head==None:
            self._head= Node(data)
            self._size += 1
        else:
            curNode= self._head
            newNode, duplicate= self.traverseNext(curNode,data)
            if duplicate == True:
                print ('item already exist, can not add into the list')
                return
            else:
                newNode.next = Node(data)
                self._size += 1
    def createChild(self,parent,child):
        isParent=False
        curNode=self._head
        if (curNode==None):
            print('list is empty, can not create a child')
            return
        else:
            while(curNode!=None):
                if (curNode.data==parent and curNode.child==None):
                    isParent=True
                    curNode.child=Node(child)
                    self._size += 1
                elif (curNode.data==parent and curNode.child!=None):
                        isParent=True

                        tmpNode = self.traverseChild(curNode.child)
                        tmpNode.child = Node(child)
                        self._size += 1
                curNode = curNode.next
            if isParent==False:
                    print('{0} does not exist as parent, therefore {1} is not added as child of {0}'.format(str(parent),str(child)))

    def printList(self):
        curNode=self._head
        while (curNode!=None):
            print(curNode.data , end=' ')
            if curNode.child!=None:
                tmpNode = curNode.child
                while (tmpNode!=None):
                    print("-> ", tmpNode.data, end=" ")
                    tmpNode = tmpNode.child

                print(" ")
            curNode=curNode.next
print("\n")
print("Task 3 output")
print("\n")
mll=multiLevelNode()
mll.createNode(1)
mll.createNode(2)
mll.createNode(3)
mll.createChild(1,2)
mll.createChild(1,3)
mll.createChild(1,8)
mll.createChild(1,9)
mll.createChild(2,4)
mll.createChild(2,5)
mll.createChild(3,6)
mll.createChild(3,7)
mll.createChild(2,10)
mll.createChild(2,11)
mll.createChild(11,12)
mll.createChild(13,14)
print("\n")
mll.printList()
