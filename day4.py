from collections import defaultdict

D = open('inputs/day4.txt').read().strip()
lines = D.split('\n')

p1 = 0
N = defaultdict(int)
for i, line in enumerate(lines):
    N[i] += 1
    first, rest = line.split('|')
    id_, card = first.split(':')
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    val = len(set(card_nums) & set(rest_nums))
    if val > 0:
        p1 += 2**(val-1)
    for j in range(val):
        N[i+1+j] += N[i]
print(p1)
print(sum(N.values()))

'''
part 1:

D = open('inputs/day4.txt').read().strip()
lines = D.split('\n')

total_sums = 0
for inde, line in enumerate(lines):
    num_of_wins = 0

    wins_dict = {}

    for win_nums in line.split(":")[1].split("|")[0].split(" "):
        if win_nums != " " and win_nums != "":
            wins_dict[win_nums] = win_nums

    print(wins_dict)

    for our_num in line.split(":")[1].split("|")[1].split(" "):
        try:
            if our_num == wins_dict[our_num]:
                print("found" + our_num)
                num_of_wins += 1
        except KeyError:
            pass

    print(f"Total number of wins: {num_of_wins}")
    print(f"Total added: {2 ** (num_of_wins - 1)}")

    if num_of_wins != 0:
        total_sums += 2 ** (num_of_wins - 1)

print(total_sums)
'''
