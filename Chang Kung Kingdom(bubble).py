t=int(input())
for i in range(t):
    count=0
    a=[int(n) for n in input().split()]
    while a!=[1,2,3]:
        for i in range(2):
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                count+=1
    print(count)