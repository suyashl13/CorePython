# A Python program to understand the various methods of array class.

from array import *

# Create an array with int values:
arr = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print('Original Array :', arr)

# Append
arr.append(30)
arr.append(60)
print('After appending 30 and 60 Array :', arr)
# Append add the appended values at end of array.

# Insert
arr.insert(1, 1000)
print('After inserting(1,1000) to Array :', arr)
# Insert inserts the value at the given index.

# Remove
arr.remove(20)
print('After removing(20) from Array :', arr)
# arr.remove(20) removes the element passed in parameters.

# POP
arr.pop()
print('After POP() on array', arr)
# arr.pop() removes the last element of the array.

# Index
index = arr.index(70)
print(arr)
print('Index of 20 in array is', index)
# index = arr.index(20) returns the index at which the element is present.

# ToList
lst = arr.tolist()
print(arr)
print(lst)