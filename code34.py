t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    days = [a, b, c]
    total = 0
    day = 0
    while total < n:
        total += days[day % 3]
        day += 1
    print(day)
#https://codeforces.com/problemset/problem/2051/B