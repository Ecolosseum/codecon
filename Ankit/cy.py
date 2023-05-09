#Write a python to form an eight of size n (with a ‘0’ in both it’s holes) with the help of Asterix (*) 
n=int(input("Enter n= "))
h=((n-1)/2)+2
m=int(n-h)
def l():
     for i in range(n-2):
         print(" ", end="")

for j in range(2):
    print(" ", end="")
    for i in range(n-2):
        print("*", end="")
    print(" ", end="")
    print()
    #first line over
    for I in range(m):
        print("*")
        l()
        print("*")
        #line escape
    print()

print(" ", end="")
for i in range(n-2):
    print("*", end="")
print(" ", end="")
