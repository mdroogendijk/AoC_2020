def main():
    magic = 2020
    i = 0
    j = 1

    with open('Day_1/input.txt') as f:
        lines = [int(line.rstrip()) for line in f]

    while True:
        if lines[i] + lines[j] == magic:
            print(lines[i] * lines[j])
            break
        elif j < (len(lines) - 1):
            j += 1
        elif j == (len(lines) - 1):
            i += 1
            j = i + 1
