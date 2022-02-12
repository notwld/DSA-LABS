class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        cur = Node(data)
        if self.head == None:
            self.head = cur
            self.tail = cur
        else:
            self.tail.next = cur
            self.tail = cur
        
    def prepend(self,data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur
    
    def insert(self,index,data):
        cur = Node(data)
        if index == 0:
            cur.next = self.head
            self.head = cur
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            cur.next = prev.next
            prev.next = cur

    def delete(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            prev.next = prev.next.next

    def traverse(self):
        cur = self.head
        while cur != None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def removeAll(self,head):
        if head == None:
            return None
        else:
            cur = head
            while cur != None:
                prev = cur
                cur = cur.next
                prev.next = None
            return cur
        
    
    def splitinHalf(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        cur = self.head
        for i in range(count//2):
            prev = cur
            cur = cur.next
        prev.next = None
        return cur
    
    def unorderedSearch(self,data):
        cur = self.head
        while cur != None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

print("--Task#01--")

link = LinkedList()
link.append(1)
link.append(2)
link.prepend(3)
link.prepend(13)
link.prepend(43)
print(link.unorderedSearch(43))
link.traverse()
print("Task#02")
print(link.splitinHalf())
link.traverse()


print("---------------------------------------------------")
            
class Bag:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,data):
        cur = Node(data)
        if self.head == None:
            self.head = cur
            self.tail = cur
        else:
            self.tail.next = cur
            self.tail = cur

    def prepend(self,data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur

    def insert(self,index,data):
        cur = Node(data)
        if index == 0:
            cur.next = self.head
            self.head = cur
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            cur.next = prev.next
            prev.next = cur

    def delete(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            prev.next = prev.next.next

    def traverse(self):
        cur = self.head
        while cur != None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def removeAll(self,head):
        if head == None:
            return None
        else:
            cur = head
            while cur != None:
                prev = cur
                cur = cur.next
                prev.next = None
            return cur
        
    def __iter__(self):
        return _BagIterator(self.head)

class _BagIterator:
    def __init__(self, head):
        self.cur = head

    def __next__(self):
        if self.cur == None:
            raise StopIteration
        else:
            data = self.cur.data
            self.cur = self.cur.next
            return data

print("LAB TASK")

bag = Bag()
bag.append(1)
bag.append(2)
bag.append(3)
bag.append(4)
bag.traverse()

class Set:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.next = None

    def append(self,data):
        #avoid duplicates
        curr = self.head
        while curr != None:
            if curr.data == data:
                return
            curr = curr.next
        cur = Node(data)
        if self.head == None:
            self.head = cur
            self.tail = cur
        else:
            self.tail.next = cur
            self.tail = cur
        
    

    def prepend(self,data):
        #avoid duplicates
        curr = self.head
        while curr != None:
            if curr.data == data:
                return
            curr = curr.next
        cur = Node(data)
        cur.next = self.head
        self.head = cur



    def insert(self,index,data):
        #avoid duplicates
        curr = self.head
        while curr != None:
            if curr.data == data:
                return
            curr = curr.next
        cur = Node(data)
        if index == 0:
            cur.next = self.head
            self.head = cur
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
        
    def delete(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            prev.next = prev.next.next

    def traverse(self):
        cur = self.head
        while cur != None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    
    def intersection(self,set1,set2):
        curr = set1.head
        while curr != None:
            if set2.unorderedSearch(curr.data):
                self.append(curr.data)
            curr = curr.next
    
    def difference(self,set1,set2):
        curr = set1.head
        while curr != None:
            if not set2.unorderedSearch(curr.data):
                self.append(curr.data)
            curr = curr.next
        
    def subset(self,set1,set2):
        curr = set1.head
        while curr != None:
            if not set2.unorderedSearch(curr.data):
                return False
            curr = curr.next
        return True

    def removeAll(self,head):
        if head == None:
            return None
        else:
            cur = head
            while cur != None:
                prev = cur
                cur = cur.next
                prev.next = None
            return cur
    
    def sortedList(self):
        cur = self.head
        while cur != None:
            prev = cur
            cur = cur.next
            if prev.data > cur.data:
                prev.next = cur.next
                cur.next = prev
                self.head = cur
                cur = prev
            else:
                prev = cur
                cur = cur.next
        return self.head
    def ordered_search(self,data):
        cur = self.head
        while cur != None:
            if cur.data == data:
                return True
            elif cur.data > data:
                return False
            else:
                cur = cur.next
        return False
    def unordered_search(self,data):
        cur = self.head
        while cur != None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def sorted_add(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.size +=1
            #print("head ",self.size)
        else:
            prev = None
            curr = self.head
            while curr and curr.data < value:
                self.size +=1
                #print("looop ",self.size)
                prev = curr
                curr = curr.next
                
            if curr !=None:
                if prev == None:
                    newnode.next = self.head
                    self.head = newnode
                #temp = prev
                  #  print("rpev = none ",self.size)
                    self.size +=1
                else:
                    
                    newnode.next = curr
                    prev.next = newnode

                 #   print("middle",self.size)
                    self.size +=1
            elif curr == None:
                prev.next = newnode
                #print("last",self.size)
                self.size +=1

    def __iter__(self):
        return _SetIterator(self.head)

class _SetIterator:
    def __init__(self, head):
        self.cur = head

    def __next__(self):
        if self.cur == None:
            raise StopIteration
        else:
            data = self.cur.data
            self.cur = self.cur.next
            return data

print("---------------------------------------------------")
print("--Task#03--")


set = Set()
set.prepend(5)
set.prepend(4)
set.prepend(1)
set.prepend(3)
set.traverse()
print("--Task#04--")
set.traverse()


print(set.unordered_search(5))
print(set.ordered_search(3))

print("---------------------------------------------------")

