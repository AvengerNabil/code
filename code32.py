t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    pos = {}
    nxt = 0
    for i in range(n):
        if a[i] == 0:
            res.append(chr(ord('a') + nxt))
            pos[res[-1]] = 1
            nxt += 1
        else:
            for ch in pos:
                if pos[ch] == a[i]:
                    res.append(ch)
                    pos[ch] += 1
                    break
    print("".join(res))
#https://codeforces.com/problemset/problem/1927/B