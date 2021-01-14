def part1(instructions):

    i = 0
    accumulator = 0

    while instructions[i]["iteration"] != 2:

        instructions[i]["iteration"] += 1

        if instructions[i]["instruction"] == "nop":
            i += 1

        elif instructions[i]["instruction"] == "acc":
            if instructions[i]["step"][:1] == "+":
                accumulator += int(instructions[i]["step"][1:])
            else:
                accumulator -= int(instructions[i]["step"][1:])
            i += 1

        elif instructions[i]["instruction"] == "jmp":
            if instructions[i]["step"][:1] == "+":
                i += int(instructions[i]["step"][1:])
            else:
                i -= int(instructions[i]["step"][1:])

    return accumulator


def part2(instructions):

    for instruction in instructions:
        if instruction["instruction"] == "nop":
            instruction["instruction"] = "jmp"

            accumulator, terminated = execute(instructions)
            if terminated:
                instruction["instruction"] = "nop"
            else:
                return accumulator
        elif instruction["instruction"] == "jmp":
            instruction["instruction"] = "nop"

            accumulator, terminated = execute(instructions)
            if terminated:
                instruction["instruction"] = "jmp"
            else:
                return accumulator

        # Reset iteration count in instructions
        for i in instructions:
            i["iteration"] = 1


def execute(instructions):

    i = 0
    accumulator = 0

    while instructions[i]["iteration"] != 2:

        instructions[i]["iteration"] += 1

        if instructions[i]["instruction"] == "nop":
            i += 1

        elif instructions[i]["instruction"] == "acc":
            if instructions[i]["step"][:1] == "+":
                accumulator += int(instructions[i]["step"][1:])
            else:
                accumulator -= int(instructions[i]["step"][1:])
            i += 1

        elif instructions[i]["instruction"] == "jmp":
            if instructions[i]["step"][:1] == "+":
                i += int(instructions[i]["step"][1:])
            else:
                i -= int(instructions[i]["step"][1:])

        if i >= len(instructions):
            terminated = False
            return accumulator, terminated

    terminated = True

    return accumulator, terminated


def main():

    file = open('Day_8/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    instructions = []

    for line in lines:
        instructions.append({"instruction": line[:3], "step": line[4:], "iteration": 1})

    # accumulator = part1(instructions)
    accumulator = part2(instructions)

    # print("The answer for part 1 is:", accumulator)
    print("The answer for part 2 is:", accumulator)
