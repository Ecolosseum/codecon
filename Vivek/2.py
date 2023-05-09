# horizontal looping
from math import ceil
i = 1
n = int(input("enter n(number of rows/columns): "))
while i <= n:
    j = 1
    while j <= n:
        if i == 1 and j == 1 or i == 1 and j == n:
            print(" ", end="")
        elif i == n and j == 1 or i == n and j == n:
            print(" ", end="")
        elif i in range(2, ceil(n/2)) and j in range(2, n):
            print(" ", end="")
        elif i in range(ceil(n/2 + 1), n) and j in range(2, n):
            print(" ", end="")
        else:
            print("*", end="")
        j += 1
    
    i = i + 1
    print()