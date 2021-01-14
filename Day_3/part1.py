def main():
    start = [0, 0]
    trees = 0

    with open('Day_3/input.txt') as f:
        lines = [line.rstrip() for line in f]

    while start[0] < len(lines):

        line = lines[start[0]]

        if line[start[1]] == '#':
            print((start[0] + 1), (start[1] + 1))
            trees += 1
        start[0] = start[0] + 1
        start[1] = start[1] + 3

        if start[1] > len(lines[0]):
            start[1] = (start[1] - len(lines[0]))
        elif start[1] == len(lines[0]):
            start[1] = 0

    print('trees:', trees)
