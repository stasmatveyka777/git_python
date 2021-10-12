a=int(input("Symma: "))
b=int(input("Procent"))
d=int(input("Mesacev"))
if d>12:
    k=d//12
    for i in range(k):
        a=a+a*(b/100)
        print(a)
else:
    print(a)
