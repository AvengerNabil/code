t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pos = [0] * (2 * n + 1)
    for i in range(n):
        pos[a[i]] = i + 1  # store 1-based index

    count = 0
    # Loop over possible a[i]
    for i in range(n):
        val_i = a[i]
        # Try all multiples of val_i that could produce i+j <= 2n
        for val_j in range(1, (2 * n) // val_i + 1):
            j = val_i * val_j - (i + 1)
            if j > i and j <= n and pos[val_j] == j:
                count += 1

    print(count)
    #https://codeforces.com/problemset/problem/1541/B