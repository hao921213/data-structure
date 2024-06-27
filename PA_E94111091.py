M=int(input())
for i in range(M):
    A=list(str(input()))
    if "." in A:
        A.remove(".")
    C=[]
    for i in range(len(A)):
        if (A[i]=='1' or A[i]=='2' or A[i]=='3' or A[i]=='4' or A[i]=='5' or A[i]=='6' or A[i]=='7' or A[i]=='8' 
               or A[i]=='9' or A[i]=='0'):
            C.append(A[i])
    B=len(C)
    odd=0
    even=0
    for i in range(0,B,2):
        even+=int(C[i])
    for j in range(1,B,2):
        odd+=int(C[j])
    if (even-odd)==0 or (abs(even-odd))%11==0:
        print("YES")
    else:
        print("NO") 