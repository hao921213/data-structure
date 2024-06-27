dis = [[float('inf')] * 7 for _ in range(7)]
dis[0][1]=dis[1][0]=50
dis[0][2]=dis[2][0]=60
dis[1][4]=dis[4][1]=90
dis[6][3]=dis[3][6]=70
dis[1][3]=dis[3][1]=120
dis[3][5]=dis[5][3]=80
dis[2][5]=dis[5][2]=50
dis[5][6]=dis[6][5]=140
dis[3][6]=dis[6][3]=70
dis[4][6]=dis[6][4]=40
for k in range(0,7):
    for i in range(0,7):
        for j in range(0,7):
            dis[i][j] = min(dis[i][j], max(dis[i][k], dis[k][j]))
t=int(input())
for _ in range(t):
    a=[int(n) for n in input().split()]
    if dis[a[0]-1][a[1]-1]==float('inf'):
        print("no path")
    else:
        print(dis[a[0]-1][a[1]-1])
    