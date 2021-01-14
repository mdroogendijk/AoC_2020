import math


def main():
    trees = []
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    with open('Day_3/input.txt') as f:
        lines = [line.rstrip() for line in f]

    for slope in slopes:
        start = [0, 0]
        hit = 0

        while start[0] < len(lines):
            line = lines[start[0]]

            if line[start[1]] == '#':
                hit += 1

            start[0] = start[0] + slope[1]
            start[1] = start[1] + slope[0]

            if start[1] > len(lines[0]):
                start[1] = (start[1] - len(lines[0]))
            elif start[1] == len(lines[0]):
                start[1] = 0

        trees.append(hit)

    result = math.prod(trees)
    print('trees:', result)
