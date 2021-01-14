def part1(my_bag, lines):
    rules = []
    containers = []
    count = 0

    for line in lines:
        line = line.replace("bags", "").replace("bag", "")

        inner = []
        outer = line.split("contain")[0].rstrip()
        content = line.split("contain")[1].lstrip().rstrip(' .')

        if content == "no other":
            inner = []

        elif ',' in content:
            bags = content.split(' , ')
            for bag in bags:
                inner.append({"color": bag[2:], "count": int(bag[0])})

        else:
            inner.append({"color": content[2:], "count": int(content[0])})

        rules.append({"outer": outer, "inner": inner})

    for rule in rules:

        if rule["inner"]:
            for bag in rule["inner"]:
                if my_bag == bag["color"]:
                    count += 1
                    containers.append(rule["outer"])
                    rules = [x for x in rules if x != rule]

    while containers:
        for container in containers:
            for rule in rules:
                if rule["inner"]:
                    for bag in rule["inner"]:
                        if container == bag["color"]:
                            count += 1
                            containers.append(rule["outer"])
                            rules = [x for x in rules if x != rule]

            containers = [x for x in containers if x != container]

    return count


def part2(my_bag, lines):
    rules = []
    containers = []
    count = 0

    for line in lines:
        line = line.replace("bags", "").replace("bag", "")

        inner = []
        outer = line.split("contain")[0].rstrip()
        content = line.split("contain")[1].lstrip().rstrip(' .')

        if content == "no other":
            inner = []

        elif ',' in content:
            bags = content.split(' , ')
            for bag in bags:
                inner.append({"color": bag[2:], "count": int(bag[0])})

        else:
            inner.append({"color": content[2:], "count": int(content[0])})

        rules.append({"outer": outer, "inner": inner})

    for rule in rules:

        if my_bag == rule["outer"]:
            for bag in rule["inner"]:
                count += bag["count"]
                containers.append({"color": bag["color"], "count": bag["count"]})
                rules = [x for x in rules if x != rule]

    while containers:
        for container in containers:
            for rule in rules:
                if (rule["inner"] != []) & (container["color"] == rule["outer"]):
                    for bag in rule["inner"]:
                        multiplied = (container["count"] * bag["count"])
                        count += multiplied
                        containers.append({"color": bag["color"], "count": multiplied})

            containers = [x for x in containers if x != container]

    return count


def main():
    my_bag = "shiny gold"

    file = open('Day_7/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    sum_bags = part1(my_bag, lines)
    required = part2(my_bag, lines)

    print("The answer for part 1 is:", sum_bags)
    print("The answer for part 2 is:", required)
