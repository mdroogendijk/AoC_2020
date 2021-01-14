import re


def byr(year):
    if (year.isdigit()) & (len(year) == 4) & (int(year) >= 1920) & (int(year) <= 2002):
        return True
    else:
        return False


def iyr(year):
    if (year.isdigit()) & (len(year) == 4) & (int(year) >= 2010) & (int(year) <= 2020):
        return True
    else:
        return False


def eyr(year):
    if (year.isdigit()) & (len(year) == 4) & (int(year) >= 2020) & (int(year) <= 2030):
        return True
    else:
        return False


def hgt(height):
    if (height[:-2].isdigit()) & (height[-2:] == "cm"):
        if (int(height[:-2]) >= 150) & (int(height[:-2]) <= 193):
            return True
        else:
            return False
    elif (height[:-2].isdigit()) & (height[-2:] == "in"):
        if (int(height[:-2]) >= 59) & (int(height[:-2]) <= 76):
            return True
        else:
            return False
    else:
        return False


def hcl(color):
    reg = re.compile('^[a-f0-9]+$')
    if (color[0] == "#") & bool(reg.match(color[1:])) & (len(color[1:]) == 6):
        return True
    else:
        return False


def ecl(color):
    if color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    else:
        return False


def pid(id_number):
    if (id_number.isdigit()) & (len(id_number) == 9):
        return True
    else:
        return False


def part1(passports):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0

    for passport in passports:

        validity = "t.b.d."

        for field in required:
            if field not in passport.keys():
                validity = "invalid"

        if validity != "invalid":
            valid += 1

    print("valid passports:", valid)


def part2(passports):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0

    for passport in passports:

        validity = "t.b.d."

        for field in required:
            if field not in passport.keys():
                validity = "invalid"
            elif not globals()[field](passport[field]):
                validity = "invalid"

        if validity != "invalid":
            valid += 1

    print("valid passports:", valid)


def main():

    file = open('Day_4/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    passports = []
    passport = {}

    for line in lines:

        if line != "":
            key_value = line.split(" ")

            for v in key_value:
                aux = v.split(":")
                passport[aux[0]] = aux[1]

            if line == lines[-1]:
                passports.append(passport)

        else:
            passports.append(passport)
            passport = {}

    # part1(passports)
    part2(passports)
