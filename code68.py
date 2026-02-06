# Read the number of buttons
n = int(input())

# Compute the worst-case number of presses: 2^n - 1
result = (1 << n) - 1  # Using bitwise shift for 2^n

# Output the result
print(result)
#https://codeforces.com/problemset/problem/268/B