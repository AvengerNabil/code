import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        w = [int(next(it)) for _ in range(n)]
        l, r = 0, n-1
        sumL, sumR = 0, 0
        ans = 0
        while l <= r:
            if sumL <= sumR:
                sumL += w[l]
                l += 1
            else:
                sumR += w[r]
                r -= 1
            if sumL == sumR:
                eaten = l + (n - 1 - r)
                if eaten > ans:
                    ans = eaten
        out_lines.append(str(ans))
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
#https://codeforces.com/problemset/problem/1669/F