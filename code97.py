# Read input
n = int(input())
original = input().strip()
target = input().strip()

moves = 0

for i in range(n):
    c = int(original[i])
    t = int(target[i])
    forward = (t - c) % 10
    backward = (c - t) % 10
    moves += min(forward, backward)

print(moves)
#https://codeforces.com/problemset/problem/540/A