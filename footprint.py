t = int(input())
for _ in range(t):
    s = input()
    length = len(s)
    arr = [0] * length

    arr[0] += 1
    next_index = int(s[0]) % length
    travel = length - 1

    while travel > 0:
        arr[next_index] += 1
        next_index = (next_index + int(s[next_index])) % length
        travel -= 1

    judge = all(i == 1 for i in arr)

    if judge:
        print("Yes")
    else:
        print("No")

    
