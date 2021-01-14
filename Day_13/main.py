def part1(busses, earliest):

    busses = [bus for bus in busses if bus != "x"]
    departure_times = {bus: 0 for bus in busses}

    for idx, bus in enumerate(busses):
        while departure_times[bus] < earliest:
            departure_times[bus] += int(bus)

    my_bus = min(departure_times, key=departure_times.get)
    waiting_time = departure_times[my_bus] - earliest

    answer = int(my_bus) * waiting_time

    return answer


def part2(busses):

    # not my own code at work :-(

    # filtered = [int(bus) for bus in busses if bus != "x"]
    # departures = {idx: [int(bus), int(bus)] for idx, bus in enumerate(busses) if bus != "x"}
    # first = departures[0][0]
    # step = max(filtered)
    # timestamp = departures[0][1]
    # all_departing = False

    busses = [(int(busses[k]), k) for k in range(len(busses)) if busses[k] != 'x']

    lcm = 1
    time = 0

    for i in range(len(busses)-1):
        bus_id = busses[i+1][0]
        idx = busses[i+1][1]
        lcm *= busses[i][0]
        while (time + idx) % bus_id != 0:
            time += lcm

    return time

#    while not all_departing:
#
#        all_departing = True
#
#        timestamp += step
#
#        if timestamp > 100000000000000:
#            for key in departures.keys():
#                if (timestamp + key) % departures[key][0] != 0:
#                    all_departing = False
#                    break
#        else:
#            all_departing = False

#    return timestamp + first


def main():

    file = open('Day_13/input.txt', 'r')
    content = file.read()
    lines = content.splitlines()

    earliest = int(lines[0])
    busses = lines[1].split(',')

    answer = part1(busses, earliest)
    timestamp = part2(busses)

    print("The answer for part 1 is:", answer)
    print("The answer for part 2 is:", timestamp)
