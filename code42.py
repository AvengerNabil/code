# Function to calculate minimum operations for one test case
def min_days(n, s, f):
    # Count the number of positions where a cat needs to be added or removed
    add = 0  # cats needed to be added
    remove = 0  # cats needed to be removed

    for i in range (n):
        if s[i] == '0' and f[i] == '1':
            add += 1
        elif s[i] == '1' and f[i] == '0':
            remove += 1

    # The minimum operations is the maximum of add and remove
    # Because we can move cats from surplus to deficit positions
    return max (add, remove)


# Read number of test cases
t = int (input ())
results = []

for _ in range (t):
    n = int (input ())
    s = input ().strip ()
    f = input ().strip ()
    results.append (min_days (n, s, f))

# Print results
for res in results:
    print (res)

#https://codeforces.com/problemset/problem/1921/B