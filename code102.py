# Read n and m
n, m = map(int, input().split())

# Build dictionary for replacement
word_map = {}
for _ in range(m):
    a, b = input().split()
    if len(a) <= len(b):
        word_map[a] = a
    else:
        word_map[a] = b

# Read the lecture
lecture = input().split()

# Output the lecture as recorded
recorded = [word_map[word] for word in lecture]
print(*recorded)
#https://codeforces.com/problemset/problem/499/B