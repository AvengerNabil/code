import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    sorted_a = sorted(a)

    possible = True
    for i in range(n):
        if (a[i] % 2) != (sorted_a[i] % 2):
            possible = False
            break

    print("YES" if possible else "NO")#https://codeforces.com/problemset/problem/1851/B