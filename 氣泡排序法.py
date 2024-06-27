#A=[int(n) for n in input().split()]
A=[2,6,2,6,8,5,2]
n=len(A)
count=0
for i in range(n-1):
    for j in range(n-1):
        if A[j]>A[j+1]:
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp
            count+=1
print(A)
print(count)
