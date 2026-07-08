t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))

    x = 0
    for v in a:
        x ^= v

    print(x)
#https://codeforces.com/problemset/problem/1698/A