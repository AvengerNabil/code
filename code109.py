n = int(input())
a = list(map(int, input().split()))

min_diff = float('inf')
idx1, idx2 = 0, 1

# Check adjacent soldiers
for i in range(n - 1):
    diff = abs(a[i] - a[i + 1])
    if diff < min_diff:
        min_diff = diff
        idx1, idx2 = i, i + 1

# Check circular pair (last and first)
circular_diff = abs(a[n - 1] - a[0])
if circular_diff < min_diff:
    idx1, idx2 = n - 1, 0

# Output 1-based indices
print(idx1 + 1, idx2 + 1)
#https://codeforces.com/problemset/problem/34/A