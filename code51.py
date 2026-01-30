import sys
import bisect

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)

it = iter(data)
n = next(it); m = next(it)
a = [next(it) for _ in range(n)]
b = [next(it) for _ in range(m)]

a.sort()
ans = [str(bisect.bisect_right(a, x)) for x in b]
print(" ".join(ans))
#https://codeforces.com/problemset/problem/600/B