M=[int(n) for n in input().split()]
A=[]
result=[]
temp=M[1]-1

for i in range(1,M[0]+1):
    A.append(i)

while len(A)>1:
    temp+=+M[2]-1
    temp=(temp%len(A))
    result.append(A[temp])
    del A[temp]

result.append(A[0])
print(*result)
