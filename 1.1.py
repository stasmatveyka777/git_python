n=int(input())
s=0
if n>0:
    while n>0:
        s=s+(1/n)
        n-=1
print(s)