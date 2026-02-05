def min_steps_to_make_divisible_by_25(n_str):
    endings = ["00", "25", "50", "75"]
    min_deletions = float('inf')
    for end in endings:
        second = end[1]
        first = end[0]
        pos2 = -1
        # Find the second digit (should be last digit of resulting number)
        for i in range(len(n_str) - 1, -1, -1):
            if n_str[i] == second:
                pos2 = i
                # Find the first digit (should be second last of resulting number)
                for j in range(pos2 - 1, -1, -1):
                    if n_str[j] == first:
                        deletions = (len(n_str) - pos2 - 1) + (pos2 - j - 1)
                        min_deletions = min(min_deletions, deletions)
                        break
    return min_deletions

# Read input and process
t = int(input())
for _ in range(t):
    n_str = input().strip()
    print(min_steps_to_make_divisible_by_25(n_str))
#https://codeforces.com/problemset/problem/1593/B