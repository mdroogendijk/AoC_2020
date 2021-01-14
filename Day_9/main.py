from itertools import combinations


def part1(lines, preamble):

    memory = []
    starting_index = 0

    for line in lines[preamble:]:

        i = 0
        memory.clear()

        while i < preamble:
            index = i + starting_index
            memory.append(lines[index])
            i += 1

        sum_possible = check_combinations(line, memory)

        if not sum_possible:
            return line
        else:
            starting_index += 1


def check_combinations(line, memory):
    for combination in combinations(memory, 2):
        if sum(combination) == line:
            return True

    return False


def part2(lines, number):

    set_length = 2
    set_sum = 0
    set_content = []

    while set_sum != number:
        for idx, line in enumerate(lines):
            end = idx + set_length
            if end < len(lines):
                contiguous = lines[idx:end]

                if sum(contiguous) == number:
                    set_content = contiguous
                    set_sum = sum(contiguous)
                    break

        set_length += 1

    weakness = min(set_content) + max(set_content)

    return weakness


def main():

    file = open('Day_9/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()
    lines = [int(x) for x in lines]

    preamble = 25

    number = part1(lines, preamble)
    weakness = part2(lines, number)

    print("The answer for part 1 is:", number)
    print("The answer for part 2 is:", weakness)
