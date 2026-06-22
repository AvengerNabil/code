t = int(input())

for _ in range(t):
    n, H, M = map(int, input().split())
    sleep_time = H * 60 + M

    ans = 1440  # max possible minutes in a day

    for _ in range(n):
        h, m = map(int, input().split())
        alarm_time = h * 60 + m

        if alarm_time >= sleep_time:
            diff = alarm_time - sleep_time
        else:
            diff = alarm_time + 1440 - sleep_time

        ans = min(ans, diff)

    print(ans // 60, ans % 60)
#https://codeforces.com/problemset/problem/1714/A