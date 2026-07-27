import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()  # empty line

    xA, yA = map(int, input().split())
    xB, yB = map(int, input().split())
    xF, yF = map(int, input().split())

    # Manhattan distance
    distance = abs(xA - xB) + abs(yA - yB)

    # Check if obstacle blocks straight path
    if xA == xB == xF:
        if min(yA, yB) < yF < max(yA, yB):
            distance += 2

    if yA == yB == yF:
        if min(xA, xB) < xF < max(xA, xB):
            distance += 2

    print(distance)
#https://codeforces.com/problemset/problem/1547/A