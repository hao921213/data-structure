def count_infected_people(M, N, grid, visited, x, y):
    if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] == '.' or visited[x][y]:
        return 0

    visited[x][y] = True
    infected_count = 1

    for i in range(-1, 2):
        for j in range(-1, 2):
            infected_count += count_infected_people(M, N, grid, visited, x + i, y + j)

    return infected_count

M, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(M)]

visited = [[False] * N for _ in range(M)]
total_infected_groups = 0

for i in range(M):
    for j in range(N):
        if grid[i][j] == 'C' and not visited[i][j]:
            infected_count = count_infected_people(M, N, grid, visited, i, j)
            if infected_count > 0:
                total_infected_groups += 1

print(total_infected_groups)
