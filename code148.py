# C. Hamburgers — Correct Python Solution

recipe = input().strip()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
r = int(input())

# Count how many of each ingredient is needed per hamburger
need_b = recipe.count('B')
need_s = recipe.count('S')
need_c = recipe.count('C')

def can_make(x):
    """
    Returns True if we can make x hamburgers with current ingredients and rubles
    """
    # Additional ingredients we need to buy
    buy_b = max(0, x * need_b - nb)
    buy_s = max(0, x * need_s - ns)
    buy_c = max(0, x * need_c - nc)

    total_cost = buy_b * pb + buy_s * ps + buy_c * pc
    return total_cost <= r

# Binary search for maximum number of hamburgers
low, high = 0, 10**13  # high large enough
ans = 0

while low <= high:
    mid = (low + high) // 2
    if can_make(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
#https://codeforces.com/problemset/problem/371/C