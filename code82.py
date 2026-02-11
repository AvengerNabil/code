t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * n

    # compute dp from right to left
    for i in range(n - 1, -1, -1):
        jump_to = i + a[i]
        if jump_to >= n:
            dp[i] = a[i]
        else:
            dp[i] = a[i] + dp[jump_to]

    print(max(dp))
#https://codeforces.com/problemset/problem/1472/C