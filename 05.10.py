a=int(input())
b=int(input())
n=0
if a<b:
    while b>=a:
        print(a)
        a=a+1
        n+=1
else:
    print('n',n)
