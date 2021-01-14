def part1(lines):

    jolts_range = range(1, 4)
    jolts = 0
    jolts_diff_1 = 0
    jolts_diff_3 = 0

    while jolts < max(lines):
        for i in jolts_range:
            if (jolts + i) in lines:

                if i == 1:
                    jolts_diff_1 += 1
                elif i == 3:
                    jolts_diff_3 += 1

                jolts += i
                break

    jolts_diff_3 += 1
    number = jolts_diff_1 * jolts_diff_3

    return number


def part2(lines):

    lines.sort()

    def awesome():
        my_dict = {0: 1}

        for line in lines:
            total = 0
            if line - 1 in my_dict:
                total += my_dict[line - 1]
            if line - 2 in my_dict:
                total += my_dict[line - 2]
            if line - 3 in my_dict:
                total += my_dict[line - 3]
            my_dict[line] = total

        return my_dict[lines[-1]]

    return awesome()


def main():

    file = open('Day_10/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()
    lines = [int(x) for x in lines]

    number = part1(lines)
    ways = part2(lines)

    print("The answer for part 1 is:", number)
    print("The answer for part 2 is:", ways)
