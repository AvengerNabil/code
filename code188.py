import sys
input = sys.stdin.readline

n = int(input())
exams = []

for _ in range(n):
    a, b = map(int, input().split())
    exams.append((a, b))

# Sort by scheduled date
exams.sort()

last_day = 0

for a, b in exams:
    if b >= last_day:
        last_day = b
    else:
        last_day = a

print(last_day)

#https://codeforces.com/problemset/problem/479/C