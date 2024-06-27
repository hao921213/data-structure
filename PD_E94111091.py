t=int(input())
for _ in range(t):
    num=int(input())
    A=[int(n) for n in input().split()]
    cla=[str(n) for n in input()]
    n=len(A)
    count=0
    for i in range(n-1):
        for j in range(n-1):
            if A[j]>A[j+1]:
                temp1=A[j]
                temp2=cla[j]
                A[j]=A[j+1]
                cla[j]=cla[j+1]
                A[j+1]=temp1
                cla[j+1]=temp2
                count+=1
    print(*A)
    print(*cla,sep='')
    print(count)
    