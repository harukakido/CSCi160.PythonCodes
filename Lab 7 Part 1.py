'''
Haruka Kido
ID #1323392
haruka.kido@ndus.edu
CSci 160. Weekly Lab 7. Part 1
intValue Functions Using Python
'''

import math
intValue = 5

#functions 1-7 with local variables
#scope 1: returns square of intValue. parameter: positive integers. return value: 25 as (5^2)
def square (intValue):
    return intValue * intValue

#scope 2: returns summation of 1 to intValue. parameter: 1-set integer. return value: 15 as (1 + 2 + 3 + 4 + 5)
def summation (intValue):
    sum = 1
    for i in range(1, intValue):
        sum = sum + 1
        sum = sum + i
    return sum

#scope 3: returns sum of the squares from 1 to intValue. parameter: 1-set integer. return value: 55 as (1 + 4 + 9 + 16 + 25)
def sumOfSquare (intValue):
    sumOfSquare = 0
    for i in range(1, intValue + 1):
        sumOfSquare = sumOfSquare + i**2
    return sumOfSquare 

#scope 4: returns factorial of 1 to intValue. parameter: 1-set integer. return value: 120 as (1 * 2 * 3 * 4 * 5)
def factorial (intValue):
    fact = 1
    for i in range(1, intValue + 1):
        fact = fact * i
    return fact

x1 = 10
y1 = 10
x2 = 5
y2 = 5

#scope 5: returns distance between two points. parameter: x and y positive integer points on coordinate plane. return value: 7.0710678118654755
def distance (x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#scope 6: returns True if intValue is odd, otherwise returns False. parameter: positive integers. return value: True
def isOdd (intValue):
    if intValue % 2 == 1:
        return True
    return False
 
#scope 7: returns True if intValue is even, otherwise returns False. parameter: positive integers. return value: False
def isEven (intValue):
    if isOdd (intValue):
        return False
    return True

#main
square = square (intValue)
summation = summation (intValue)
sumsq = sumOfSquare (intValue)
fact = factorial (intValue)
dist = distance (x1, y1, x2, y2)
odd = isOdd (intValue)
even = isEven (intValue)

#assigns the functions' local variables into global variables
#calls functions to print 

print(square)
print(summation)
print(sumsq)
print(fact)
print(dist)
print(odd)
print(even)

