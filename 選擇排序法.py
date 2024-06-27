A=[3,2,1]
n=len(A)
count=0
for i in range(n):
    min=i
    for j in range(i,n):
        if A[min]>A[j]:
            min=j
    temp=A[i]
    A[i]=A[min]
    A[min]=temp
    count+=1
print(A)
print(count)

