M=int(input())
while(M!=0):
    A=int(input())
    B=list(map(int,input().split(' ')))
    max=1
    for i in range(A):
        for j in range(A):
            m=min(B[i],B[j])
            if max<m*(j-i):
                max=m*(j-i)
    print(max)
    M-=1