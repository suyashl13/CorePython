# CH:3 Operators in Python.
##########################################################

# Arithmetic Operators.
a = 5
b = 15

print('Addition Operator => +')
print(a)
print(b)
print('a + b :', a + b)

print('Subtraction Operator => -')
print(a)
print(b)
print('a - b :', a - b)

print('Division Operator => /')
print(a)
print(b)
print('a / b :', a / b)

print('Division Operator (Returns Integer quotient only.) => //')
print(a)
print(b)
print('a // b :', a // b)

print('Modulus Operator (Returns remainder of division) => %')
print(a)
print(b)
print('a % b :', a % b)

print('Exponention Operator => ** ')
print(a)
print(b)
print('a ** b :', a ** b)
##########################################################

# Assignment Operators.

print('Assigning same value to two different variables.')

# Method 1
x = y = 1
print(x, y)


# Method 2
x = 1; y = 2
print(x, y)

# Method 3
a, b = 1, 2
print(x, y)

# Swapping two numbers..
m = 12
n = 21

m, n = n, m
print(m, n)
##########################################################

# Relational Operators

a = 152
b = 153
c = 153

print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print( a != b)
##########################################################

# Boolean Operators.

a = True
b = False

print(a and b)
print(a or b)
print(not b)
