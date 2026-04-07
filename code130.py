t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(n):
        parts = input().split()
        b = int(parts[0])
        moves = parts[1]
        u = moves.count('U')
        d = moves.count('D')
        delta = (u - d) % 10
        orig = (a[i] - delta + 10) % 10  # ensure positive
        res.append(orig)
    print(*res)
#https://codeforces.com/problemset/problem/1703/C