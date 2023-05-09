def D(n):
    x = 0.0
    y = 1.0
    for i in range(1,int(n)+1,1):
        tmp = (-1)**i * (1/i)
        print(tmp)
        if tmp < 0:
            x += tmp
        else:
            y += tmp
    return [x,y]

n1 = D(float(input('=>')))
x1 = n1[0]
y1 = n1[1]

n2 = D(float(input('=>')))
x2 = n2[0]
y2 = n2[1]

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

print("Distance from position ({0},{1}) to position ({2},{3}) is {4}".format(x1,y1,x2,y2,distance))