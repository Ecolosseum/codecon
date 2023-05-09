#question1
try:
    x1=int(input("Enter x co-ordinate of first point"))
    y1=int(input("Enter y co-ordinate of first point"))
    x2=int(input("Enter x co-ordinate of second point"))
    y2=int(input("Enter y co-ordinate of second point"))
    dis=((x2-x1)**2+(y2-y1)**2)**1/2
    print("Distance b/w the points is",dis)
except:
    print("Error")


#question2
n=int(input("Enter size of the 8"))
b="0"
for i in range(1,n*2):
    if i==1 or i==n or i==n*2:
        for j in range(1,n+1):
            if j==1 or j==n:
                print("*")
            else:
                print(end=" ")
    else:
        for k in range(1,n+1):
            if k==1 or k==n+1:
                print("*")
            else:
                print(end=" ")
