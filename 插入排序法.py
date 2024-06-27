A=[4,7,3,6,1,9,6,0]
n=len(A)
for i in range(1,n):
    temp=A[i]
    j=i-1
    while j>=0 and temp<A[j]:
        A[j+1]=A[j]
        j-=1
    A[j+1]=temp
print(A)