t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    count = 0
    i = 0
    while i + k <= n:
        # check if segment [i, i+k) has only zeros
        if prefix[i + k] - prefix[i] == 0:
            count += 1
            i += k + 1  # hike + rest
        else:
            i += 1

    print(count)
#https://codeforces.com/problemset/problem/2126/B