n, m = map(int, input().split())

count = 0

for a in range(1001):
    for b in range(1001):
        if a * a + b == n and a + b * b == m:
            count += 1

print(count)
#https://codeforces.com/problemset/problem/214/A