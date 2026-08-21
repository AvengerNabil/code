import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    team_size = 0
    teams = 0

    for skill in arr:
        team_size += 1

        if team_size * skill >= x:
            teams += 1
            team_size = 0

    print(teams)
    #https://codeforces.com/problemset/problem/2091/B