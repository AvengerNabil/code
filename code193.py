import sys

input = sys.stdin.readline

q = int(input())

for _ in range(q):
    n = int(input())
    t = input().strip()

    i = n - 1
    result = []

    while i >= 0:
        if t[i] == '0':
            num = int(t[i - 2:i])
            result.append(chr(num + 96))
            i -= 3
        else:
            num = int(t[i])
            result.append(chr(num + 96))
            i -= 1

    print("".join(result[::-1]))#https://codeforces.com/problemset/problem/1729/B