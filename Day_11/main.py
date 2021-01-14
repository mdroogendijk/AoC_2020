def part1_swapping(current):

    future = []

    for row_id, row in enumerate(current):

        future_row = []

        for idx, seat in enumerate(row):
            if seat == "L":
                possible = True
                if idx + 1 < len(row):
                    if row[idx + 1] not in ["L", "."]:
                        possible = False

                    if row_id + 1 < len(current):
                        if current[row_id + 1][idx + 1] not in ["L", "."]:
                            possible = False

                    if row_id - 1 >= 0:
                        if current[row_id - 1][idx + 1] not in ["L", "."]:
                            possible = False

                if idx - 1 >= 0:
                    if row[idx - 1] not in ["L", "."]:
                        possible = False

                    if row_id + 1 < len(current):
                        if current[row_id + 1][idx - 1] not in ["L", "."]:
                            possible = False

                    if row_id - 1 >= 0:
                        if current[row_id - 1][idx - 1] not in ["L", "."]:
                            possible = False

                if row_id + 1 < len(current):
                    if current[row_id + 1][idx] not in ["L", "."]:
                        possible = False

                if row_id - 1 >= 0:
                    if current[row_id - 1][idx] not in ["L", "."]:
                        possible = False

                if possible:
                    future_row.append("#")
                else:
                    future_row.append("L")

            elif seat == ".":
                future_row.append(".")

            elif seat == "#":

                adjacent = 0

                if idx + 1 < len(row):
                    if row[idx + 1] == "#":
                        adjacent += 1

                    if row_id + 1 < len(current):
                        if current[row_id + 1][idx + 1] == "#":
                            adjacent += 1

                    if row_id - 1 >= 0:
                        if current[row_id - 1][idx + 1] == "#":
                            adjacent += 1

                if idx - 1 >= 0:
                    if row[idx - 1] == "#":
                        adjacent += 1

                    if row_id + 1 < len(current):
                        if current[row_id + 1][idx - 1] == "#":
                            adjacent += 1

                    if row_id - 1 >= 0:
                        if current[row_id - 1][idx - 1] == "#":
                            adjacent += 1

                if row_id + 1 < len(current):
                    if current[row_id + 1][idx] == "#":
                        adjacent += 1

                if row_id - 1 >= 0:
                    if current[row_id - 1][idx] == "#":
                        adjacent += 1

                if adjacent >= 4:
                    future_row.append("L")
                else:
                    future_row.append("#")

        future = future[:] + [future_row]

    if current == future:
        return future, True
    else:
        return future, False


def part2_swapping(current):

    future = []

    for row_id, row in enumerate(current):

        future_row = []

        for idx, seat in enumerate(row):
            if seat == "L":
                possible = True

                i = idx + 1
                loop = True
                while (i < len(row)) & loop:
                    if row[i] == "#":
                        possible = False
                        loop = False
                    elif row[i] == "L":
                        loop = False
                    else:
                        i += 1

                i = idx + 1
                j = row_id + 1
                loop = True
                while (i < len(row)) & (j < len(current)) & loop:
                    if current[j][i] == "#":
                        possible = False
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i += 1
                        j += 1

                i = idx + 1
                j = row_id - 1
                loop = True
                while (i < len(row)) & (j >= 0) & loop:
                    if current[j][i] == "#":
                        possible = False
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i += 1
                        j -= 1

                i = idx - 1
                loop = True
                while (i >= 0) & loop:
                    if row[i] == "#":
                        possible = False
                        loop = False
                    elif row[i] == "L":
                        loop = False
                    else:
                        i -= 1

                i = idx - 1
                loop = True
                j = row_id + 1
                while (i >= 0) & (j < len(current)) & loop:
                    if current[j][i] == "#":
                        possible = False
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i -= 1
                        j += 1

                i = idx - 1
                loop = True
                j = row_id - 1
                while (i >= 0) & (j >= 0) & loop:
                    if current[j][i] == "#":
                        possible = False
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i -= 1
                        j -= 1

                loop = True
                j = row_id + 1
                while (j < len(current)) & loop:
                    if current[j][idx] == "#":
                        possible = False
                        loop = False
                    elif current[j][idx] == "L":
                        loop = False
                    else:
                        j += 1

                loop = True
                j = row_id - 1
                while (j >= 0) & loop:
                    if current[j][idx] == "#":
                        possible = False
                        loop = False
                    elif current[j][idx] == "L":
                        loop = False
                    else:
                        j -= 1

                if possible:
                    future_row.append("#")
                else:
                    future_row.append("L")

            elif seat == ".":
                future_row.append(".")

            elif seat == "#":

                adjacent = 0

                i = idx + 1
                loop = True
                while (i < len(row)) & loop:
                    if row[i] == "#":
                        adjacent += 1
                        loop = False
                    elif row[i] == "L":
                        loop = False
                    else:
                        i += 1

                i = idx + 1
                j = row_id + 1
                loop = True
                while (i < len(row)) & (j < len(current)) & loop:
                    if current[j][i] == "#":
                        adjacent += 1
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i += 1
                        j += 1

                i = idx + 1
                j = row_id - 1
                loop = True
                while (i < len(row)) & (j >= 0) & loop:
                    if current[j][i] == "#":
                        adjacent += 1
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i += 1
                        j -= 1

                i = idx - 1
                loop = True
                while (i >= 0) & loop:
                    if row[i] == "#":
                        adjacent += 1
                        loop = False
                    elif row[i] == "L":
                        loop = False
                    else:
                        i -= 1

                i = idx - 1
                loop = True
                j = row_id + 1
                while (i >= 0) & (j < len(current)) & loop:
                    if current[j][i] == "#":
                        adjacent += 1
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i -= 1
                        j += 1

                i = idx - 1
                loop = True
                j = row_id - 1
                while (i >= 0) & (j >= 0) & loop:
                    if current[j][i] == "#":
                        adjacent += 1
                        loop = False
                    elif current[j][i] == "L":
                        loop = False
                    else:
                        i -= 1
                        j -= 1

                loop = True
                j = row_id + 1
                while (j < len(current)) & loop:
                    if current[j][idx] == "#":
                        adjacent += 1
                        loop = False
                    elif current[j][idx] == "L":
                        loop = False
                    else:
                        j += 1

                loop = True
                j = row_id - 1
                while (j >= 0) & loop:
                    if current[j][idx] == "#":
                        adjacent += 1
                        loop = False
                    elif current[j][idx] == "L":
                        loop = False
                    else:
                        j -= 1

                if adjacent >= 5:
                    future_row.append("L")
                else:
                    future_row.append("#")

        future = future[:] + [future_row]

    if current == future:
        return future, True
    else:
        return future, False


def part1(grid):

    occupied = 0
    unchanged = False
    current = grid

    while not unchanged:
        future, unchanged = part1_swapping(current)
        current = future

    for i in current:
        occupied += i.count("#")

    return occupied


def part2(grid):

    occupied = 0
    unchanged = False
    current = grid

    while not unchanged:
        future, unchanged = part2_swapping(current)
        current = future

    for i in current:
        occupied += i.count("#")

    return occupied


def main():

    file = open('Day_11/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()
    grid = []

    def split(row):
        return [char for char in row]

    for line in lines:
        grid.append(split(line))

    occupied = part1(grid)
    occupied_again = part2(lines)

    print("The answer for part 1 is:", occupied)
    print("The answer for part 2 is:", occupied_again)
