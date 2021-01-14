def main():
    magic = 2020
    i = 0
    j = 1
    k = 1

    with open('Day_2/input.txt') as f:
        lines = [int(line.rstrip()) for line in f]

    while True:
        if lines[i] + lines[j] + lines[k] == magic:
            print(lines[i] * lines[j] * lines[k])
            break
        elif j < (len(lines) - 1):
            j += 1
        elif k < (len(lines) - 1):
            k += 1
            j = i + 1
        elif k == (len(lines) - 1):
            i += 1
            k = i + 1
