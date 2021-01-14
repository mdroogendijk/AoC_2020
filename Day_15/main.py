def part1(numbers):

    magic_number = 2020
    last_spoken = 0
    spoken = []
    i = 0

    for number in numbers:
        spoken.append(number)
        last_spoken = number
        i += 1

    while i != magic_number:

        if spoken.count(last_spoken) > 1:
            idx = [i for i, x in enumerate(spoken) if x == last_spoken]
            diff = idx[-1] - idx[-2]
            spoken.append(diff)
            last_spoken = diff

        else:
            spoken.append(0)
            last_spoken = 0

        i += 1

    answer = spoken[-1]

    return answer


def part2(numbers):

    magic_number = 2020
    # last_spoken = 0
    spoken = {}
    previous = {}
    i = 1
    last_spoken = 0

    for number in numbers:
        spoken[number] = i
        i += 1
        last_spoken = number

    # last_spoken = 0

    while i < 11:
        if last_spoken in previous:
            diff = spoken[last_spoken] - previous[last_spoken]
            print(diff)

            if diff in spoken:
                previous[diff] = spoken[diff]

            spoken[diff] = i

        else:
            previous[last_spoken] = spoken[last_spoken]
            spoken[last_spoken] = i -1
            last_spoken = 0

        print(i, last_spoken, previous, spoken)

        # print(spoken)
        # print(i, last_spoken)
        i += 1

    answer_part2 = last_spoken

    return answer_part2


def main():

    file = open('Day_15/sample.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    numbers = {int(x): "" for x in lines[0].split(',')}

    answer = part1(numbers)
    answer_part2 = part2(numbers)

    print("The answer for part 1 is:", answer)
    print("The answer for part 2 is:", answer_part2)
