import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, l, r = map(int, input().split())

    right = min(r, m)
    left = m - right

    l_prime = -left
    r_prime = right

    print(l_prime, r_prime)#https://codeforces.com/problemset/problem/2094/B