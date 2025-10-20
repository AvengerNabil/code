def suneet_wins(a1, a2, b1, b2):
    from itertools import permutations
    suneet_cards = [a1, a2]
    slavic_cards = [b1, b2]
    win_count = 0

    for s_order in permutations(suneet_cards):
        for b_order in permutations(slavic_cards):
            s_wins = 0
            b_wins = 0
            for s_card, b_card in zip(s_order, b_order):
                if s_card > b_card:
                    s_wins += 1
                elif b_card > s_card:
                    b_wins += 1
            if s_wins > b_wins:
                win_count += 1
    return win_count

# Read input
t = int(input())
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    print(suneet_wins(a1, a2, b1, b2))
