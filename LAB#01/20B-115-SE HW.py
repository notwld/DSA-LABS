class Counter:
    def __init__(self):
        self.count = 0
    
    def counter(self):
        self.count=self.count+1

    def showCount(self):
        return self.count

    def reset(self):
        self.count=0

hui = Counter()
hui.counter()
hui.counter()
hui.counter()
hui.counter()

print(hui.showCount())

from random import choice as su
class GrabBag:
    def __init__(self):
        self.items = ["surf","cloths","owo","owo","uwu"]
    
    def grabItem(self):
        self.items.remove(su(self.items))
    
    def showShow(self):
        return self.items

obj = GrabBag()
print(obj.showShow())
obj.grabItem()
print(obj.showShow())


class GrabBag2(GrabBag):

    def numOf(self,item):
        o = 0
        for each in self.items:
            if each == item:
                o +=1
        return f"no of {item} is {o}"


obj2 = GrabBag2()
print(obj2.numOf("owo"))

class StudentFileReader:
    def __init__(self,file):
        self.file = open(file,"r")
        self.content = self.file.read().split("\n")

    def showContent(self):
        print(" ,".join(self.content[0:5]))
        print(" ,".join(self.content[5:10]))
        print(" ,".join(self.content[10:15]))
        print(" ,".join(self.content[15:20]))

file = StudentFileReader("file1.txt")
file.showContent()

class StudentFileWriter(StudentFileReader):
    def __init__(self,file,file2):
        self.file = open(file,"r")
        self.content = self.file.read().split("\n")
        self.output = open(file2,'w')
    
    def writeContent(self):
        self.output.write(" ,".join(self.content[0:5])+"\n")
        self.output.write(" ,".join(self.content[5:10])+"\n")
        self.output.write(" ,".join(self.content[10:15])+"\n")
        self.output.write(" ,".join(self.content[15:20]))

out = StudentFileWriter("file1.txt","file2.txt")
out.writeContent()

from math import sqrt

class lineSegment:
    def __init__(self,ptA,ptB):
        self.point1 = ptA
        self.point2 = ptB

    def endPointA(self): 
        eA=("x1=",self.point1[0],"y1=",self.point1[1])
        return eA

    def endPointB(self): 
        eB=("x2=",self.point2[0],"y2=",self.point2[1])
        return eB
    def _str_(self):
        return "({0} , {1}) , ({2} , {3})".format(self.point1[0],self.point1[1],self.point2[0],self.point2[1])
        
    def length(self):
        return sqrt(((self.point1[0]-self.point2[0])*2)+((self.point1[1]-self.point2[1])*2))

    def isVartical(self):
        if self.point1[0]==self.point2[0]:
            return ("Line is verticle")
        else:
            return ("Line is not verticle")
        
    def isHorizontal(self):
        if self.point1[1]==self.point2[1]:
            return ("Line is Horizontal")
        else:
            return ("Line is not Horizontal")
        
    
    def midpoint(self):
        return ((self.point1[0]+self.point2[0])//2,(self.point1[1]+self.point2[1])//2)

    def slope(self):
        return (self.point2[1]-self.point1[1])/(self.point2[0]-self.point1[0])
    
    def isParallel(self,other):
        if self.slope()==other.slope():
            return True
        else:
            return False
    
    def isPerpendicular(self,other):
        if self.slope()==-1/other.slope():
            return True
        else:
            return False
    def bisects(self,other):
        if self.isParallel(other):
            return False
        else:
            return True
    
    def intersection(self,other):
        if self.bisects(other):
            return True
        else:
            return False
    
    def shift(self,x,y):
        self.point1[0]+=x
        self.point1[1]+=y
        self.point2[0]+=x
        self.point2[1]+=y
        return (self.point1,self.point2)

p1 = lineSegment([1,2],[11,5])
p2 = lineSegment([1,2],[5,5])
print(p1.isVartical())
print(p1.isParallel(p2))
print(p1.isPerpendicular(p2))
print(p1.intersection(p2))
print(p1.bisects(p2))
print(p1.shift(2,3))
print(p1.slope())
print(p1.isParallel(p2))


