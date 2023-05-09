def pattern(n):
    for i in range(1,n-1):
        print('*',end='')
    for i in range((n//2)):
        print('*'+' '*(n-2)+'*')
    for i in range(1,n+1):
        print('*',end='')
    for i in range((n//2)):
        print('*'+' '*(n-2)+'*')
    for i in range(1,n-1):
        print('*',end='')
n=int(input('Enter number:'))
if n%2!=0:
    pattern(n)
else:
    ('Please enter an odd number')
    
