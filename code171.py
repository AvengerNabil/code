n = int(input())
a = list(map(int, input().split()))

INF = 10**9
dp = [[INF] * 3 for _ in range(n + 1)]

# Base case
dp[0][0] = dp[0][1] = dp[0][2] = 0

for i in range(1, n + 1):
    today = a[i - 1]

    # Rest
    dp[i][0] = min(dp[i - 1]) + 1

    # Contest
    if today == 1 or today == 3:
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])

    # Gym
    if today == 2 or today == 3:
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n]))
#https://codeforces.com/problemset/problem/698/A