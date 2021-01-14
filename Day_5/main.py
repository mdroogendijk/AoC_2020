def part1(seats):

    return max(seats)


def part2(seats):

    seats.sort()

    for seat in seats:
        center = seat + 1
        right = seat + 2

        if (center not in seats) & (right in seats):
            return center


def get_row(line):

    row = range(0, 127)

    for character in line:
        middle_index = (len(row) // 2)
        if character == "F":
            row = row[:middle_index]
        elif character == "B":
            row = row[middle_index:]

    if row:
        row = row[0] + 1
        return row
    else:
        return 0


def get_column(line):

    column = range(0, 7)

    for character in line:
        middle_index = (len(column) // 2)
        if character == "L":
            column = column[:middle_index]
        elif character == "R":
            column = column[middle_index:]

    if column:
        column = column[0] + 1
        return column
    else:
        return 0


def main():

    file = open('Day_5/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    seats = []

    for line in lines:

        row = get_row(line[:7])
        column = get_column(line[-3:])

        seat = (row * 8 + column)
        seats.append(seat)

    highest = part1(seats)
    seat = part2(seats)

    print("The answer for part 1 is:", highest)
    print("The answer for part 2 is:", seat)
