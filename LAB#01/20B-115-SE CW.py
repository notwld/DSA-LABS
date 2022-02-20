def is_multiple(n,m):
    assert n>m
    if n%m==0:
        return True
    return False

print(is_multiple(25,5))

def isEven(k):
    return k & 1

n = 2
if isEven(n) == 0:
    print("Even")
else:
    print("Odd")

def EvenList(n):
    li = list()
    for i in range(n):
        value = int(input("Enter Value: "))
        if value%2==0:
            li.append(value)

    return li

print(EvenList(4))
    

def minmax(data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]>data[j]:
                data[i],data[j] = data[j],data[i]
    return (data[0],data[-1])

print(minmax([2,5,89,1,3]))

def sequence(n):
    sum = 0
    for i in range(n):
        if n>0:
            sum = i**2
    return sum

print(sequence(7))

def sumoddsquares(k):
    odd = []
    for i in range(len(k)):
        if k[i]%2==1:
            odd.append(k[i])
    sq = [i**2 for i in odd]
    return sum(sq)

print(sumoddsquares([3,5,7,6,2]))

def distincOddPairGen(array):
    odd = []
    pairs = []
    for i in array:
        for j in array:
            mul = i*j
            if mul % 2!=0:
                odd.append((i,j))
    return odd

print(distincOddPairGen([1,2,3]))

def Reverse(li):
    return li[::-1]

print(Reverse([1,2,3]))
    
def Unique(li):
    u = []
    for i in range(len(li)):
        if li[i] not in u:
            u.append(li[i])
    return u

print(Unique([4,4,5,6,7,5,2,3]))

def UserNumber(n):
    li = []
    for i in range(n):
        o = int(input("Enter value: "))
        if o%2==0:
            li.append(o)

    return (li[-1],max(li),min(li),li[-2])

print(UserNumber(10))

def ShowExcitement():
    for i in range(5):
        print("A quick brown fox jumps over the lazy dog.",end=" ")

ShowExcitement()
print('\n')
def Greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        pass

print(Greater(3,5,1))

def Divide(n,m):
    return (n/m,n%m)

print(Divide(5,4))

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def birthday(self):
        self._age += 1
        return self._age

    def name(self):
        return self._name


obj = Person("goju saturo",20)
print(obj.birthday())





