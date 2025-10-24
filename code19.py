t = int(input())
for _ in range(t):
    n = int(input())
    efficiencies = list(map(int, input().split()))
    missing_efficiency = -sum(efficiencies)
    print(missing_efficiency)

#https://codeforces.com/problemset/problem/1877/A