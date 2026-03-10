t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    k = d - b  # diagonal moves

    if k < 0:
        print(-1)
        continue

    l = a + k - c  # left moves

    if l < 0:
        print(-1)
    else:
        print(k + l)
#https://codeforces.com/problemset/problem/1806/A