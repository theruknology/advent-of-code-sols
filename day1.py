D = open('inputs/day1.txt').read().strip()
words_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total_num = 0

for line in D.split('\n'):
    print('at line')
    indi = 0
    first_digit = ""
    last_digit = 0
    while indi < len(line) and first_digit == "":
        if line[indi] in "1234567890":
            first_digit = int(line[indi])
            break

        for d, val in enumerate(words_list):
            if line[indi:].startswith(val):
                first_digit = d+1
                break
        indi += 1

    while indi < len(line):
        if line[indi] in "1234567890":
            last_digit = line[indi]
        for d, val in enumerate(words_list):
            if line[indi:].startswith(val):
                last_digit = d+1
                break
        indi += 1

    last_digit = int(last_digit)

    total_num += (first_digit * 10) + last_digit
    print(line)

print(total_num)
