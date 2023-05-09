import math

# To calculate factorial 
def factorial(n):
    if (n==0 or n==1):
        return 1
    else :
        return (n* factorial(n-1))


# Main code

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
n1fact = factorial(num1)
n2fact = factorial(num2)

x1 = float (0)
y1 = float(0)
x2 = float (0)
y2 = float(0)

# For 1st Number
for i in range(0,num1):
    if (i//2 != 0):
        x1 = float(x1 -  1/factorial(i))
    else :
        y1 = float(y1  + 1/factorial(i))

# For 2nd Number
for j in range(0,num2):
    if (j//2 != 0):
        x2 = float(x2 -  1/factorial(j))
    else :
        y2 = float(y2  + 1/factorial(j))


distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(distance)




