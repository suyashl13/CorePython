# Loop keywords :

# 1.Break keyword:

print('Break Keyword \n')
str = "Suyash"

for i in str:
    print(i)
    if i == 'y':
        break

# Another Example:
print('Break Keyword \n')

for i in range(1, 10):
    print(i)
    if i == 5:
        break

#  Continue Keyword :

print('Continue Keyword \n')

for i in range(20, 0, -1):
    print(i)
    if i <= 10:
        print('Now "i" is smaller than 10')
        continue

print('Continue Keyword \n')

for i  in range(0,20):
    print(i)
    if i < 10:
        continue

#  Pass Keyword:

for i in range(20):
    pass # Do nothing

# A

