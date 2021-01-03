# CH:4 Input and Output in Python

# More Printing :-

name = 'linda'
lName = 'nike'
someList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 21, 0]

print('hai %s' % name)
print('hai (%20s)' % name)
print(name, lName, sep=':')

for i in someList:
    print(i, end=' ')

print('\n', list(range(10)))

print('What is your name ?')
name = input('>>')
print('Hello,', name)

print('Enter two numbers')
a = int(input('>>'))
b = int(input('>>'))
print(f'Sum = {a + b}')