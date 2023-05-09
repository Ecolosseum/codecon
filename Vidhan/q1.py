import math

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

array = [1,2,3,4]
output = []

def fib_dearranments(n):
    
    if n == 1 or n == 0: return 0
    if n == 2: return 1
    else:
        return  (n-1)*(fib_dearranments(n-1) + fib_dearranments(n-2))
        



for i in array:
    output.append(fib_dearranments(i))



def breaking_and_dist(n):
    #break number into negative and positive
    x = 0
    y = 0
    
    for j in range(n+1):
        value = (-1)**j / math.factorial(j)
        if j%2 == 0:
            y += value
        else:
            x += value
    
    return x,y

x , y = breaking_and_dist(l)
print((x-n1)**2 + (y-n2)**0.5)