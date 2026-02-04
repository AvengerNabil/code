n = int(input())
# In the worst-case scenario, Manao will have to try all sequences like in Tower of Hanoi
# The formula for the minimum number of pushes in the worst case is 2^n - 1
print((1 << n) - 1)
#https://codeforces.com/problemset/problem/268/B