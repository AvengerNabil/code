import math

q = int(input())

for _ in range(q):
    s = input().strip()
    t = input().strip()

    l = math.lcm(len(s), len(t))

    s1 = s * (l // len(s))
    s2 = t * (l // len(t))

    if s1 == s2:
        print(s1)
    else:
        print(-1)
#https://codeforces.com/problemset/problem/1473/B 