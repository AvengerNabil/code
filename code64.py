import sys
import math

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

# target position from s1
target = s1.count('+') - s1.count('-')

# known position from s2 and number of unknowns
known = s2.count('+') - s2.count('-')
q = s2.count('?')

# we need k pluses among q unknowns such that:
# known + (2*k - q) == target  =>  k = (target - known + q) / 2
diff = target - known
if q == 0:
    prob = 1.0 if diff == 0 else 0.0
else:
    # compute required k
    if (diff + q) % 2 != 0:
        prob = 0.0
    else:
        k = (diff + q) // 2
        if 0 <= k <= q:
            favourable = math.comb(q, k)
            prob = favourable / (2 ** q)
        else:
            prob = 0.0

print("{:.12f}".format(prob))
#https://codeforces.com/problemset/problem/476/B