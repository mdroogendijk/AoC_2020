def main():
    total = 0

    with open('Day_2/input.txt') as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        occurrence = 0
        low = int(line.split('-')[0])
        high = int(line.split('-')[1].split(' ')[0])
        letter = line.split(' ')[1].split(':')[0]
        password = line.split(': ')[1]

#        print(low, high, letter, password)
        for character in password:
            if character == letter:
                occurrence += 1

        if (occurrence >= low) & (occurrence <= high):
            total += 1

    print(total)
