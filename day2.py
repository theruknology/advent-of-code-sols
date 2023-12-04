D = open('inputs/day2.txt').read().strip()

guidelines = [12, 13, 14]
total_pow = 0

for i, line in enumerate(D.split('\n')):

    data = line.split(":")[1]

    highest_red = 1
    highest_green = 1
    highest_blue = 1

    for blocks in data.split(';'):
        for si_data in blocks.split(','):
            amount = int(si_data.split(" ")[1])
            if "red" in si_data:
                if highest_red < amount:
                    highest_red = amount
            if "green" in si_data:
                if highest_green < amount:
                    highest_green = amount
            if "blue" in si_data:
                if highest_blue < amount:
                    highest_blue = amount

    total_pow += highest_red*highest_green*highest_blue

print(total_pow)
