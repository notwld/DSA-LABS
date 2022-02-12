import ctypes
import random

class Array:
    def __init__(self,size):
        
        assert size > 0,"Size 0 cannot be accepted"
        
        self.size = size
        
        pyarray = ctypes.py_object * self.size
        self.element = pyarray()
        
        self.clear(None)
        
    def __len__(self):
        return self.size
    def clear(self,val):
        
        for i in range(len(self.element)):
            self.element[i] = val
            
            
    def __getitem__(self,index):
        assert index <= self.size and index >=0,"index out of range"
        
        return self.element[index]
    
    def __setitem__(self,index,val):
        assert index < self.size and index >=0,"index out of range"
        
        self.element[index] = val
    
    
    
    
    
class MatrixLinked:
    def __init__(self,col,value):
        self.column = col
        self.data = value
        self.next = None

    

class sparsematrix:
    def __init__(self,rows,cols):
        self.rows = Array(rows)
        
        self.col = cols
        
    def numofrows(self):
        return len(self.rows)
    def numofcol(self):
        return (self.col)
    
    
    
    
    def __getitem__(self,indextpl):
        assert len(indextpl) == 2, "Wrong index"
        
        row = indextpl[0]
        col = indextpl[1]
        
        assert row <= self.numofrows() and row >= 0,"Index out of range"
        curr = self.rows[row]
        
        while curr and curr.column != col:
            curr = curr.next
            
        if curr != None:
            return curr.data
        
    def __setitem__(self,indextpl,val):
        
        assert len(indextpl) == 2, "Wrong index"
        
        row = indextpl[0]
        col = indextpl[1]
        
        
        prev = None
        curr = self.rows[row]
        
        while curr and curr.column != col:
            prev = curr
            curr = curr.next
            
        if curr is not None and curr.column == col:
            if val == 0:
                if curr == self.rows[row]:
                    self.rows[row] = curr.next
                    
                else:
                    prev.next = curr.next
            else:
                curr.data = val
        elif val != 0 :
            newnode = MatrixLinked(col,val)
            
            if curr == self.rows[row]:
                self.rows[row] = newnode
                
            else:
                newnode.next = curr
                prev.next = newnode
                
                
    def scaleby(self,scalar):
        for r in range(self.numofrows()):
            currnode = self.rows[r]
            
            while currnode:
                currnode *= scalar
                currnode = currnode.next
    def traverse(self):
        
        for r in range(self.numofrows()):
            currnode = self.rows[r]
            
            
            print(" ")
            #print("Row",r)
            print("")
            #print("Row:{}\nCol:{} Data:{}".format(r,currnode.column,currnode.data),end="  ")
            while currnode:
                print(currnode.data,end=" ")
                #print(currnode.)
                currnode = currnode.next
                
    def transpose(self,mat):
    
        newmat = sparsematrix(mat.numofrows(),mat.numofcol())
        
        for r in range(mat.numofrows()):
            for c in range(mat.numofcol()):
                newmat[r,c] = mat[c,r]
                
                
        return newmat.traverse()           
                
    def __add__ ( self , rhsMatrix ) :
        

        newMatrix = sparsematrix ( self.numofrows() , self.numofcol() )
        for row in range ( self.numofrows() ) :
            curNode = self.rows[ row ]
            while curNode is not None :
                newMatrix [ row , curNode.column ] = curNode.data
                curNode = curNode.next

        for row in range ( rhsMatrix.numofrows() ) :
            curNode = rhsMatrix.rows[ row ]
            while curNode is not None :
                value = newMatrix [ row , curNode.column ]
                value += curNode.data
                newMatrix [ row , curNode.column ] = value
                curNode = curNode.next

        return newMatrix
    
    
    def __sub__ ( self , rhsMatrix ) :
        

        newMatrix = sparsematrix ( self.numofrows() , self.numofcol() )
        for row in range ( self.numofrows() ) :
            curNode = self.rows[ row ]
            while curNode is not None :
                newMatrix [ row , curNode.column ] = curNode.data
                curNode = curNode.next

        for row in range ( rhsMatrix.numofrows() ) :
            curNode = rhsMatrix.rows[ row ]
            while curNode is not None :
                value = newMatrix [ row , curNode.column ]
                value -= curNode.data
                newMatrix [ row , curNode.column ] = value
                curNode = curNode.next

        return newMatrix



                

        
obj = sparsematrix(2,2)        


for i in range (obj.numofrows()):
    
    for j in range(obj.numofcol()):
        
        
        
        obj[i,j] = random.randint(1,9)
        
print()



print(f"Traverse:")
obj.traverse()


print()
print(f"Transpose:")
obj.transpose(obj)

obj1 = sparsematrix(2,2)    
for i in range (obj1.numofrows()):
    
    for j in range(obj1.numofcol()):
        
        obj1[i,j] = random.randint(1,9)
        
      
    

c =obj-obj1
print()

print(f"Subtraction:")
c.traverse()





# Task#02

class Polynomial:
    def __init__(self, degree = None, coefficient = None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead


    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree
    def coffient(self):
        if self._polyHead is None:
            return 0
        else:
            return self._polyHead.coefficient
    def __getitem__(self, degree):
        assert self.degree() >= 0, \
            "Operation not permitted in empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next
        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.degree

    def evaluate(self, scalar):
        assert self.degree() >= 0, \
            "Only non-empty polynomials can be evaluated!"
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
            "Addition only allowed in non-empty Polynomials"
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = self._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                #adds when degree is same
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next
            #if the list itself is longer
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly


    def __sub__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
            "Addition only allowed in non-empty Polynomials"
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = self._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                
                #print(nodeA.degree)
                degree = nodeA.degree
                value = nodeA.coefficient - nodeB.coefficient
                #adds when degree is same
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        while nodeA is not None:
            
            print("hola ",degree)
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next
            #if the list itself is longer
        while nodeB is not None:
            print("hola ",degree)
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly

    def __mul__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
            "Multiplication only allowed in non-empty Polynomials"
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = self._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree + nodeB.degree
                value = nodeA.coefficient * nodeB.coefficient
                #adds when degree is same
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)
        

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next
            #if the list itself is longer
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly

    #Helper method for appending terms in the polynomial
    def _appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm
            self._polyTail = newTerm
        
    def evaluate_poly(self, x):
        assert self.degree() >= 0, \
            "Only non-empty polynomials can be evaluated!"
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (x ** curNode.degree)
            curNode = curNode.next
        return result


class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
    
print("\n\nTask#02\n\n")
eq1 = Polynomial(2,6)

eq2 = Polynomial(2,6)
print("Degree of eq 1 before addition : ",eq1.degree())
print("Coefficient of eq 1 before addition : ",eq1.coffient())

print("Degree of eq 2 before addition : ",eq2.degree())
print("Coefficient of eq 2 before addition : ",eq2.coffient())

new = eq2 + eq1

print("Degree of eq 1 after addition : ",new.degree())
print("Coefficient of eq 1 after addition : ",new.coffient())

print("Degree of eq 2 after addition : ",new.degree())
print("Coefficient of eq 2 after addition : ",new.coffient())

new2 = eq2 - eq1

print("Degree of eq 2 after subtraction : ",new2.degree())
print("Coefficient of eq 2 after subtraction : ",new2.coffient())
new3 = eq1 * eq2

print("Degree of eq 2 after subtraction : ",new3.degree())
print("Coefficient of eq 2 after subtraction : ",new3.coffient())