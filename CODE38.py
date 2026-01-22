import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # If all elements are already ≤ d
    if a[-1] <= d:
        print("YES")
    # Otherwise, if the sum of the two smallest elements is ≤ d,
    # we can always use them to replace larger elements
    elif a[0] + a[1] <= d:
        print("YES")
    else:
        print("NO")
#https://codeforces.com/problemset/problem/1473/A