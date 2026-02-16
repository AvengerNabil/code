import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
out_lines = []
for _ in range(t):
    b = data[idx:idx+7]; idx += 7
    a1 = b[0]
    a2 = b[1]
    a3 = b[6] - a1 - a2
    out_lines.append(f"{a1} {a2} {a3}")
print("\n".join(out_lines))
#https://codeforces.com/problemset/problem/1618/A