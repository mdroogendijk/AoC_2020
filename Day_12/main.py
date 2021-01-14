import math


def rotate(xy, radians):

    x, y = xy
    xx = round(x * math.cos(radians) + y * math.sin(radians))
    yy = round(-x * math.sin(radians) + y * math.cos(radians))

    return xx, yy


def move_direction_part1(coordinates, action, direction):

    movement = int(action[1:])

    if action[0] == "N":
        coordinates[1] = coordinates[1] + movement

    elif action[0] == "S":
        coordinates[1] = coordinates[1] - movement

    elif action[0] == "E":
        coordinates[0] = coordinates[0] + movement

    elif action[0] == "W":
        coordinates[0] = coordinates[0] - movement

    elif action[0] == "L":
        direction -= movement
        if direction < 0:
            direction += 360

    elif action[0] == "R":
        direction += movement
        if direction >= 360:
            direction -= 360

    elif action[0] == "F":
        # North
        if direction == 0:
            coordinates[1] = coordinates[1] + movement
        # East
        elif direction == 90:
            coordinates[0] = coordinates[0] + movement
        # South
        if direction == 180:
            coordinates[1] = coordinates[1] - movement
        # West
        if direction == 270:
            coordinates[0] = coordinates[0] - movement

    return coordinates, direction


def move_direction_part2(ship, waypoint, action):

    movement = int(action[1:])
    direction = 0

    if action[0] == "N":
        waypoint[1] = waypoint[1] + movement

    elif action[0] == "S":
        waypoint[1] = waypoint[1] - movement

    elif action[0] == "E":
        waypoint[0] = waypoint[0] + movement

    elif action[0] == "W":
        waypoint[0] = waypoint[0] - movement

    elif action[0] == "L":
        direction -= movement
        # if direction < 0:
        #    direction += 360
        waypoint[0], waypoint[1] = rotate(waypoint, math.radians(direction))

    elif action[0] == "R":
        direction += movement
        # if direction >= 360:
        #    direction -= 360
        waypoint[0], waypoint[1] = rotate(waypoint, math.radians(direction))

    elif action[0] == "F":
        ship = [(ship[0] + waypoint[0] * movement), (ship[1] + waypoint[1] * movement)]

    return ship, waypoint, direction


def part1(actions):

    start = [0, 0]
    coordinates = start
    direction = 90

    for action in actions:
        coordinates, direction = move_direction_part1(coordinates, action, direction)

    absolute_coordinates = [abs(coordinate) for coordinate in coordinates]
    distance = sum(absolute_coordinates)

    return distance


def part2(actions):

    start = [0, 0]
    waypoint = [10, 1]
    ship = start

    for action in actions:
        ship, waypoint, direction = move_direction_part2(ship, waypoint, action)

    absolute_coordinates = [abs(coordinate) for coordinate in ship]
    distance = sum(absolute_coordinates)

    return distance


def main():

    file = open('Day_12/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    distance = part1(lines)
    distance2 = part2(lines)

    print("The answer for part 1 is:", distance)
    print("The answer for part 2 is:", distance2)
