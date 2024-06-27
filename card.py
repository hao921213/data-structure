N=int(input())
M=int(input())
while(M!=0):
    A=[]
    B = list(map(int,input().split(' ')))
    count=-1
    num=0
    for j in range(1,N+1):
        count+=1
        A.append(j)
        while(count>=0 and B[num]==A[count]):
            A.pop()
            num+=1
            count-=1
    if num==N:
        print("Yes")
    else:
        print("No")
    M-=1


    