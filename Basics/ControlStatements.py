# CH 6 Control Statements
import math

r = float(input('Enter radius of circle >> '))

area = math.pi * r ** 2
print('Area of circle =', area)

# 1. If Statement.

# Syntax :
# if condition:
#   statements
# Program :

marks = int(input('Marks >> '))
if marks > 89:
    print('Great Job !!')
elif marks > 70:
    print('fist class dist')
elif marks > 35:
    print('Pass')
elif marks < 35:
    print('fail')

# Another Example :
someValue = int(input('Some Number >> '))
anotherValue = int(input('Another Number >> '))
if someValue == 1:
    print(1)
    if anotherValue == 2:
        print(2)
        print('I am nested..')
else:
    print('Nothing interesting.')

# Loops :
# While Loops :
# Example :

loopNumber = int(input('Enter the number times you want to loop through..'))
x = 0
while x <= loopNumber :
    print(x)
    x = x + 1

# An another loop.

x = 0
while x <= 20:
    print(f'{x} itteration')
    x = x + 1
    print('End')

# The For Loop..
str = 'Suyash'

for ch in str:
    print(ch.capitalize(), end=' ')

# looping in range :

for i in range(0, 10):
    print(i)

# Looping in descending order :

for i in range(10, 0, -1):
    print(i)

list = [20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in list:
    print(i)

# Nested Loops...

for  i in range(3):
    for j in range(5):
        print('i =',i , ' j =', j)
