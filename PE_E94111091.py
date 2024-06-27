M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
d = [[0] * N for _ in range(M)]
maxs = 0  
for i in range(M):
    d[i][0] = matrix[i][0]
    maxs = max(maxs, d[i][0])
for j in range(N):
    d[0][j] = matrix[0][j]
    maxs = max(maxs, d[0][j])
for i in range(1, M):
    for j in range(1, N):
        if matrix[i][j] == 1:
            d[i][j] = min(min(d[i - 1][j], d[i][j - 1]), d[i - 1][j - 1]) + 1
            maxs = max(maxs, d[i][j])
        else:
            d[i][j] = 0
print(maxs * maxs)