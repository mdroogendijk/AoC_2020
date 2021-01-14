def part1(lines):

    counts = 0
    groups = []
    positive = []

    for num, line in enumerate(lines, start=1):

        if line != "":

            for character in line:
                if character not in positive:
                    positive.append(character)

            if num == len(lines):
                groups.append(positive)

        else:
            groups.append(positive)
            positive = []

    for group in groups:
        counts += len(group)

    return counts


def part2(lines):

    counts = 0
    persons = 0
    unique = []
    positive = []

    for num, line in enumerate(lines, start=1):

        if line != "":

            persons += 1

            for character in line:
                if character not in unique:
                    unique.append(character)

                positive.append(character)

            if num == len(lines):
                for item in unique:
                    if persons == positive.count(item):
                        counts += 1

        else:
            for item in unique:
                if persons == positive.count(item):
                    counts += 1
            positive = []
            unique = []
            persons = 0

    return counts


def main():

    file = open('Day_6/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    sum_anyone = part1(lines)
    sum_everyone = part2(lines)

    print("The answer for part 1 is:", sum_anyone)
    print("The answer for part 2 is:", sum_everyone)
