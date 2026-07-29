import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    people = list(zip(b, a))
    people.sort()  # sort by share cost ascending

    total_cost = p  # inform first person directly
    informed = 1  # number of informed people

    for cost, max_share in people:
        if informed >= n:
            break

        if cost >= p:
            break

        can_inform = min(max_share, n - informed)
        total_cost += can_inform * cost
        informed += can_inform

    # Remaining people informed directly
    if informed < n:
        total_cost += (n - informed) * p

    print(total_cost)
#https://codeforces.com/problemset/problem/1876/A