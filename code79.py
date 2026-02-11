t = int(input())  # number of test cases
for _ in range(t):
    a, b = map(int, input().split())
    x = a & b
    result = (a ^ x) + (b ^ x)
    print(result)
#https://codeforces.com/problemset/problem/1421/A