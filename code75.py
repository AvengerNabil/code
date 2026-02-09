t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    found = False
    for j in range(1, n - 1):  # j from 2 to n-1 in 1-indexed terms
        if p[j - 1] < p[j] > p[j + 1]:
            print("YES")
            print(j, j + 1, j + 2)  # Convert to 1-indexed
            found = True
            break
    if not found:
        print("NO")
#https://codeforces.com/problemset/problem/1380/A