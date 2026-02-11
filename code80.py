# C. Little Girl and Maximum Sum

n, q = map(int, input().split())
a = list(map(int, input().split()))

freq = [0] * (n + 1)

for _ in range(q):
    l, r = map(int, input().split())
    freq[l - 1] += 1
    if r < n:
        freq[r] -= 1

# prefix sum to calculate frequency count per index
for i in range(1, n):
    freq[i] += freq[i - 1]

freq.pop()  # remove extra element

# sort both lists
a.sort()
freq.sort()

# calculate maximum sum
result = sum(x * y for x, y in zip(a, freq))

print(result)
#https://codeforces.com/problemset/problem/276/C