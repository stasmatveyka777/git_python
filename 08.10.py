x=float(input("x= "))
b=float(input("b= "))
if x<=-2:
    if b>=0:
        y=3*x**2-8*b
    else:
        y=-9*x**2-12*b
else:
    y=32+x
print("y=",y)
