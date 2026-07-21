import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    s = list(map(int, input().split()))

    left, right = 1, 10**9
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        total = 0

        for x in s:
            total += (x + 2 * mid) ** 2
            if total > c:
                break

        if total == c:
            ans = mid
            break
        elif total < c:
            left = mid + 1
        else:
            right = mid - 1

    print(ans)
#https://codeforces.com/problemset/problem/1850/E