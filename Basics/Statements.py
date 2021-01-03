# Statements

# 1.The assert statement:

x = int(input('Enter any value greater than 0 >> '))

try:
    assert x > 0, "Wrong input entered."
    print('You entered', x)

except AssertionError:
    print('Wrong input entered.')

# Another Example:

y = int(input('Enter any even number >> '))
try:
    assert y % 2 == 0, "You Entered an odd number !"
    print('You entered an even number', y)
except AssertionError:
    print('You entered an odd number', y)


# 2.Return Statement:

def add(a, b):
    return a + b


print(add(23, 45))


# Another Example

def sub(a, b):
    return print(a - b)


sub(55, 20)