import random
from matplotlib import pyplot as plt
import numpy as np
from timeit import Timer
print("task 1")
def version1 ( n ) :
    totalSum = 0 # Version 1
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 , n ) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            totalSum = totalSum + matrix [i , j ]
            counter +=2
    return counter
def version2 ( n ) :
    totalSum = 0 # Version 2
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 ,n ,1) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            counter +=1
        totalSum = totalSum + rowSum [ i ]
        counter +=1
    return counter

def simulation1 ( n ) :
    steps_version1 =[0]* n
    steps_version2 = [0] * n
    for i in range (0 , n ) :
        steps_version1 [ i ]= version1 ( i )
        steps_version2 [ i ]= version2 ( i )
    x = list ( range ( n ) )
    plt . plot (x , steps_version2 )
    plt . plot (x , steps_version1 )
    plt . grid ( which ='both')
    plt . xlabel ('Input Size (n)')
    plt . ylabel ('Number of Steps ')
    plt . legend ([ 'version2' ,'version1'])
    plt . show ()

simulation1(50)
print("task 2")
def concatenation () :
    l = []
    for i in range (1000):
        l = l + [ i ]
def append () :
    l = []
    for i in range (1000):
        l.append ( i )

def comprehension () :
    l = [ i for i in range (1000) ]

def rangeFunction () :
    l = list ( range (1000) )

t1 = Timer ("concatenation()", "from __main__ import concatenation ")
concatTime = t1 . timeit ( number =1000)
print ("concatination", concatTime , "milliseconds")
t2 = Timer ("append()", "from __main__ import append")
appendTime = t2 . timeit ( number =1000)
print ("append", appendTime , "milliseconds")
t3 = Timer ("comprehension ()", "from __main__ import comprehension")
compTime = t3 . timeit ( number =1000)
print ("comprehension", compTime , "milliseconds")
t4 = Timer ("rangeFunction()", "from __main__ import rangeFunction")
rangeTime = t4 . timeit ( number =1000)
print (" list range ", rangeTime , " milliseconds ")
fig = plt . figure ()
ax = fig . add_axes ([0 ,0 ,1 ,1])
langs = [ 'concatination', "append ",  "comprehension" , "Range" ]
students = [ concatTime , appendTime , compTime , rangeTime ]
ax . bar ( langs , students )
plt . show ()

#task 3
print("task 3")
def ex1 ( n ) :
    totalSum = 0
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 , n ) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            totalSum = totalSum + matrix [i , j ]
            counter +=2
    return counter
def ex2 ( n ) :
    totalSum = 0
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 ,n ,1) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            counter +=1
        totalSum = totalSum + rowSum [ i ]
        counter +=1
    return counter
def ex3 ( n ) :
    totalSum = 0 
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 , n ) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            totalSum = totalSum + matrix [i , j ]
            counter +=2
    return counter
def ex4 ( n ) :
    totalSum = 0 
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 ,n ,1) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            counter +=1
        totalSum = totalSum + rowSum [ i ]
        counter +=1
    return counter
def ex5 ( n ) :
    totalSum = 0 
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 , n ) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            totalSum = totalSum + matrix [i , j ]
            counter +=2
    return counter
def ex6 ( n ) :
    totalSum = 0
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 ,n ,1) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            counter +=1
        totalSum = totalSum + rowSum [ i ]
        counter +=1
    return counter
def ex7 ( n ) :
    totalSum = 0 
    matrix = np . random . randint (10 , size =( n , n ) )
    rowSum =[0]* n
    counter =3 
    for i in range (0 , n ) :
        rowSum [ i ] = 0
        counter +=1
        for j in range (0 , n ) :
            rowSum [ i ] = rowSum [ i ] + matrix [i , j ]
            totalSum = totalSum + matrix [i , j ]
            counter +=2
    return counter
def simulation ( n ) :
    steps_ex1 = [0] * n
    steps_ex2 = [0] * n
    steps_ex3 = [0] * n
    steps_ex4 = [0] * n
    steps_ex5 = [0] * n
    steps_ex6 = [0] * n
    steps_ex7 = [0] * n
    for i in range (0 , n ) :
        steps_ex1 [i]=ex1( i )
        steps_ex2 [i]=ex2( i )
        steps_ex3 [i]=ex3( i )
        steps_ex4 [i]=ex4( i )
        steps_ex5 [i]=ex5( i )
        steps_ex6 [i]=ex6( i )
        steps_ex7 [i]=ex7( i )
    x = list ( range ( n ) )
    plt . plot (x , steps_ex1 )
    plt . plot (x , steps_ex2 )
    plt . plot (x , steps_ex3 )
    plt . plot (x , steps_ex4 )
    plt . plot (x , steps_ex5 )
    plt . plot (x , steps_ex6 )
    plt . plot (x , steps_ex7 )
    plt . grid ( which ='both')
    plt . xlabel ('Input Size (n)')
    plt . ylabel ('Number of Steps ')
    plt . legend ([ 'ex1' ,'ex2','ex3','ex4','ex5','ex5','ex6','ex7'])
    plt . show ()
simulation(50)



print("task 4")
lst = []

for i in range(1000):
    lst.append(i)
    


newlst = []

b = []
w = []
a = []
def sel(value):

    global newlst
    
    
    random.shuffle(lst)
    
    newlst.append(lst.index(value))
    
    
    
def simulation3 ( n, vakue ) :
    global b
    global w
    global a
    global newlst
    
    
    for i in range (0 , n ) :
        sel(vakue)
        b.append(min(newlst))
        w.append(max(newlst))
        a.append(sum(newlst)//n)
        
    x = list ( range ( n ) )
    plt . plot (x , b )
    plt . plot (x , w )
    plt . plot (x , a )
    
    plt . grid ( which ='both')
    plt . xlabel ('Input Size (n)')
    plt . ylabel ('Number of Steps ')
    plt . legend ([ 'worst' ,'best'])
    plt . show ()

simulation3(40,3)