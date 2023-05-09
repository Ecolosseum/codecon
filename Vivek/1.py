from math import sqrt
def fact(x):
    i = 1
    p = 1
    while i <= x:
        p = p * i
        i = i + 1
    return p

def get_points(n):
    x = 0
    y = 0
    for i in range(0, n+1, 1):
        if i % 2 == 0:
            y += (1/fact(i))
        elif i % 2 == 1:
            x += (1/fact(i))
    return (x,y)

def point_distance(p1, p2): # distance between two points p1 and p2
        square_add = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
        return sqrt(square_add)

if __name__ == "__main__":
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))
    print(point_distance(get_points(n1), get_points(n2)))