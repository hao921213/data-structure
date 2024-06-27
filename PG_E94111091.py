def fa(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fa(n - 1)
def fi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(2,n+1):
            temp=a+b
            a=b
            b=temp
        return b
m=int(input())
results=[]
for _ in range(m):
    n=int(input())
    results.append(fi(fa(n)%19))
for result in results:
    print(result)