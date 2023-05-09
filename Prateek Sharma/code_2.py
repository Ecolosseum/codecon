def draw(n):

    #position determination for zero placement
    z1,z2 = 0,0
    if ((n+1)/2)%2 == 0:
        z1 = ((n+1)/2)-1
        z2 = ((3/2)*(n+1))-1
    else:
        z1 = ((n+1)/2)
        z2 = ((3/2)*(n+1))-2

    #8 draw start
    for y in range(1,n*2):
        if y%2 == 1:
            for x in range(1,n+1):

                #first and last row
                if y in (1,(n*2)-1):
                    if x in (1,n):
                        print(" ",end = "")
                    else:
                        print("*", end="")

                #zero in the middle    
                elif y in (z1,z2):
                    if x in (1,n):
                        print("*",end="")
                    elif x == (n+1)/2:
                        print("0",end = "")
                    else:
                        print(" ",end="")

                #middle full line
                elif y == n:
                    print("*",end = "")
                
                #borders
                else:
                    if x in (1,n):
                        print("*",end="")
                    else:
                        print(" ",end="")
                        
        #to add a new line and change rows
        print("")


n = int(input())

#checking odd symmetric
if n%2 == 0:
    print("ERROR! try using an odd value")
else:
    draw(n)