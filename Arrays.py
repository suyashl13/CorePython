# CH.7: Arrays in Python.
import array

a = array.array('i', [21, 35, 65, -8, 69, 54, 2])

print('The array elements are :')

for element in a:
    print(element, end=' ')

# Program 2 :

ar = [5, 3, 5, -9]

for element in ar:
    print(element)

# Program 3 : Creating the array arr2 same as arr1

arr1 = array.array('d', [1.5, 2.3, 65.5, 45, 4.52])
arr2 = array.array(arr1.typecode, (a * 3 for a in arr1))

print('\n')
for element in arr2:
    print(element)

# Program 4 : Displaying using while loop

arr3 = [45, 25, 62, 36, 15, 23, 53]

x = 0
n = len(arr3)
print('\n')
while x < n:
    print(arr3[x], end=' ')
    x += 1

# Program 4 : Slicing of arrays.

arr = [12, 21, 35, 56, 53]
print(arr)
a = arr[:4]
print('\n')
print(a)

b = arr[2:]
print(b)

c = arr[1:2]
print(c)

