t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)  # sort descending
    print(*a)
#https://codeforces.com/problemset/problem/1312/B