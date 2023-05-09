size = int(input())
if size%2 == 0:
    size += 1
height = size-3

print(('*'*(size - 2)).center(size))

for x in range(0,int(height/2),1):
    if int(height/4) - 1 == x:
        print((' '*(size - 5) + '0' + ' '*(size - 5)).center(size,'*'))
    else:
        print((' '*(size - 2)).center(size,'*'))

print('*'*size)

for x in range(1,int(height/2)+1,1):
    if int(height/4) + 1 == x:
        print((' '*(size - 5) + '0' + ' '*(size - 5)).center(size,'*'))
    else:
        print((' '*(size - 2)).center(size,'*'))

print(('*'*(size-2)).center(size))