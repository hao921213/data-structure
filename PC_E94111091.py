t = int(input())
r = []
for _ in range(t):
    n = int(input())
    b = list(range(1, n + 1))
    count = 0
    a = [int(x) for x in input().split()]
    while a != b:
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                count += 1

    r.append(count)
for result in r:
    print(result)
