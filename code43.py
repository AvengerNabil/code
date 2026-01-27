import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        out.append("Alice" if (a + b) % 2 == 1 else "Bob")
    print("\n".join(out))

if __name__ == "__main__":
    solve()
#https://codeforces.com/problemset/problem/1919/A