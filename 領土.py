M = [(int(n)for n in input().split())]
map_data = []
for _ in range(M[0]):
    row = [int(n) for n in input().split()]
    map_data.append(row)

result = []

for i in range(M[0]):
    temp = []
    for j in range(M[1]):
        if map_data[i][j] == 1:
            if i == 0 or i == M[0] - 1 or j == 0 or j == M[1] - 1:
                temp.append(0)
            elif (
                map_data[i + 1][j] == 0
                or map_data[i - 1][j] == 0
                or map_data[i][j + 1] == 0
                or map_data[i][j - 1] == 0
            ):
                temp.append(0)
            else:
                temp.append("_")
        else:
            temp.append("_")
    result.append(temp)

for row in result:
    print(*row)
