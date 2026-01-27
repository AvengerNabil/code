n, b, d = map(int, input().split())
oranges = list(map(int, input().split()))

waste = 0
empties = 0

for size in oranges:
    if size <= b:
        waste += size
        if waste > d:
            empties += 1
            waste = 0

print(empties)
#https://codeforces.com/problemset/problem/709/A