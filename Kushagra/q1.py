import math

n1 = int(input("enter n1"))
n2 = int(input("enter n2"))

r = True
if n1 or n2 <=0:
    print("invalid input")
    r = False
    

def fact(num_fact):
    fact_num = 1
    if num_fact == 0:
        return 1
    
    elif num_fact < 0:
        return 0

    else:

        for num_fact1 in range(1,num_fact + 1):
            fact_num = fact_num*num_fact1
        return fact_num
    

    
def der_x(num_derx):
    x = 0
    for i in range(1,num_derx+1,2):
        x += 1/fact(i)

    return x

def der_y(num_dery):
    y = 0
    for j in range(2,num_dery+1,2):
        y +=1/fact(j)

    return y

def distance(x1,y1,x2,y2):
    d = (((x2 - x1)**2) + ((y2 - y1)**2))
    return math.sqrt(d)

while r == True:
    a = der_x(n1)
    b = der_y(n1)
    c = der_x(n2)
    d = der_y(n2)

    print(distance(a,b,c,d))
    break