n = int(input("Enetr a odd number "))

k = (n//2)+1
# To get the middle line 
m = (k//2)
# For the zero 
l = n-m+1

if (n%2 == 1):
    for i in range (1,n+1):
        for j in range(1,n+1):
            if (i ==1 or i ==k or i==n or j ==1 or j==n ):
                print("*", end= "")
            elif ( j==k and (i ==m or i==l)  ):
                print("0",end="")                
            else:
                print(" ",end="")
        print()
else:
    print("Wrong Input")