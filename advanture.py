M=int(input())
for i in range(M):
    A=list(str(input()))
    A.remove(".")
    B=len(A)
    odd=0
    even=0
    for i in range(0,B,2):
        even+=int(A[i])
    for j in range(1,B,2):
        odd+=int(A[j])
    if (even-odd)==0 or (abs(even-odd))%11==0:
        print("YES")
    else:
        print("NO") 