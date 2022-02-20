class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, data):
        curNode = DNode(data)
        if self.head == None:
            self.head = curNode
            self.tail = curNode
        elif data < self.head.data:
            curNode.next = self.head
            self.head.prev = curNode
            self.head = curNode
        elif data > self.tail.data:
            self.tail.next = curNode
            curNode.prev = self.tail
            self.tail = curNode
        else:
            node = self.head
            while node.next != None and node.next.data < data:
                node = node.next
            curNode.next = node
            curNode.prev = node.prev
            node.prev.next = curNode
            node.prev = curNode
            
        
        self.size += 1

    def remove(self, data):
        node = self.head
        while node != None:
            if node.data == data:
                if node.prev == None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                if node.next == None:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
                self.size -= 1
                return
            node = node.next
        raise ValueError("Data not found")
    
    def search(self,target):
        node = self.head
        if target < node.data:
            while node != None and target<=node.data:
                if node.data == target:
                    return True
                else:
                    node = node.prev
        else:
            while node != None and target>=node.data:
                if node.data == target:
                    return True
                else:
                    node = node.next

        return False

    def traverse(self):
        node = self.head
        while node != None:
            print(node.data, end="->")
            node = node.next
        print("None")
        return


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

dlink = DLinkedList()
dlink.add("A")
dlink.add("B")
dlink.add("C")
dlink.add("D")

dlink.traverse()
print(dlink.head.next.data)
print(dlink.search("X"))
dlink.remove("B")
dlink.traverse()