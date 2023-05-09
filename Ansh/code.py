def endline(n):
    S = " "
    for i in range(0,n-2):
        S += "*"
    S += " "
    return S

def spaceline(n):
    S = ""
    for i in range(0,n):
        S += " "
    return S

def midline(n,zero=False):
    S = "*"
    for i in range(0,n-2):
        if (i + 1) == (n-1)/2 and zero:
              S += "0"
        else:
            S += " "
    S += "*"
    return S

n = 0

while True:
    n = int(input("enter the size: "))

    if n%2 == 0:
        print("please enter a odd value for size")
    else:
        break

if ((n-1)/2)%2 == 0:
    Z = ((n-1)/2)
else:
    Z = ((n-1)/2) - 1

for i in range(0,(2*n)-1):
    if i == 0 or i == n-1 or i == (2*n)-2:
        print(endline(n))
    else:
        if i%2 == 0:
            if i == Z or i == (2*n) - 2*Z:
                print(midline(n,True))
            else:
                print(midline(n))
        else:
            print(spaceline(n))
            
            
    
