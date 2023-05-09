import math
n=int(input("Enter number for derangement:"))
D=[]
t=1
l=1
for i in range(1,n+1):
    l*=i
    t=((-1)**(i-1))*(1/l)
    D.append(t)
x=0
y=0
for i in D:
    if i<0:
        x+=i
    else:
        y+=i
n1=eval(input("Enter number 1:"))
n2=eval(input("Enter number 2:"))
dist=math.sqrt((x-n1)**2+(y-n2)**2)
print(dist)

