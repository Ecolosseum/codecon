#function to calculate factorial
def fact(x):
    a = 1
    for i in range(1,x+1):
        a *= i
    return a

#returns the coordinates as a tuple (x,y)
def coords(n):
    a,b = 1,0
    x,y = 0,0

    while a<=n:
        x += (1/fact(a))
        a += 2

    while b<=n:
        y += (1/fact(b))
        b += 2
    
    #multiplied by -1 to convert to negative factor neglected earlier
    return((x*(-1),y))

#distance formula application on returned tuples
def distance(a,b):
    xd = (a[0]-b[0])**2                 #calculates (x1-x2)^2
    yd = (a[1]-b[1])**2                 #calculates (y1-y2)^2
    d = (xd+yd)**(1/2)                  #calculates final distance
    return d

n1 = int(input())
n2 = int(input())

#coordinates from inputted numbers
c1 = coords(n1)
c2 = coords(n2)

#prints distance value rounded to 4 decimal places
print(round(distance(c1,c2),4))





