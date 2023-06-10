# while loops

count = 0
while count < 5:
    print('hello world')
    count += 1
print('end of loop')

# for loops
for i in range(5):
    print('hello world from for loop')
print('end of for loop')


print('')

print('How many times do you want to print \'hello world\'')
count = int(input())
for i in range(count):
    print('hello world')
print('exiting loop')
