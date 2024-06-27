C = []
index1 = [int(n) for n in input().split()]
A = []
for _ in range(index1[0]):
    row = [int(n) for n in input().split()]
    A.append(row)
index2 = [int(n) for n in input().split()]
B = []
for _ in range(index2[0]):
    row = [int(n) for n in input().split()]
    B.append(row)
for i in range(index1[0]):
    row=[]
    for j in range(index2[1]):
        count=0
        for k in range(index1[1]):
            count+=A[i][k]*B[k][j]
        row.append(count)
    C.append(row)
for i in range(index1[0]):
        print(*C[i])