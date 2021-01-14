def main():
    total = 0

    with open('Day_2/input.txt') as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        first = int(line.split('-')[0])-1
        second = int(line.split('-')[1].split(' ')[0])-1
        letter = line.split(' ')[1].split(':')[0]
        password = line.split(': ')[1]

        if (password[first] == letter) ^ (password[second] == letter):
            total += 1
            print(password[first], password[second], letter, password)

    print(total)
