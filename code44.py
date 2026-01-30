n = int(input())
pages = list(map(int, input().split()))

day = 0
while n > 0:
    n -= pages[day]
    if n <= 0:
        print(day + 1)
        break
    day = (day + 1) % 7
#https://codeforces.com/problemset/problem/139/A