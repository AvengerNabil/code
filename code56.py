t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print("0 0")
        continue
    diff = abs(a - b)
    moves = min(a % diff, diff - a % diff)
    print(diff, moves)
#https://codeforces.com/problemset/problem/1543/A