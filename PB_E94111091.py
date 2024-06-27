t=int(input())
for _ in range(t):
    M=[int(n) for n in input().split()]
    node=M[0]
    edge=M[1]
    test=M[2]
    dis = [[float('inf')] * node for _ in range(node)]
    for i in range(edge):
        temp=[int(n) for n in input().split()]
        dis[temp[0]-1][temp[1]-1]=dis[temp[1]-1][temp[0]-1]=temp[2]
    for k in range(0,node):
        for i in range(0,node):
            for j in range(0,node):
                dis[i][j] = min(dis[i][j], max(dis[i][k], dis[k][j]))
    for _ in range(test):
        a =[int(n) for n in input().split()]
        if dis[a[0]-1][a[1]-1]==float('inf'):
            print("no path")
        else:
            print(dis[a[0]-1][a[1]-1])