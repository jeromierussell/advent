from functools import reduce
from fractions import gcd


def lcm(a, b):
    return a * b / gcd(a, b)


def lcms(*numbers):
     return reduce(lcm, numbers)


def gcds(*numbers):
     return reduce(gcd, numbers)


def read_file():
    with open('./input/advent_day_13_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    return raw_lines


def yo():
    lines = """939
7,13,x,x,59,x,31,19""".splitlines()

    lines = read_file()

    t = int(lines[0])
    # filter out 'x' and convert to int
    busses = map(int, [i for i in lines[1].split(",") if i != 'x'])

    max_time = max(busses)

    schedule = {}
    for i in range(t, t + max_time):
        for bus in busses:
            if i % bus == 0:
                if schedule.get(i):
                    schedule.get(i).append(bus)
                else:
                    new_sched = [bus]
                    schedule[i] = new_sched

    # print(t)
    # print(busses)
    # print(schedule)

    min_key = min(schedule.keys())
    earliest_bus = schedule[min_key][0]

    print("Answer 1 => " + str(earliest_bus * abs(min_key - t)))


def yo2_slow():
    # test cases
    lines = "\n7,13,x,x,59,x,31,19".splitlines()
    # lines = "\n17,x,13,19".splitlines()
    # lines = "\n1789,37,47,1889".splitlines()

    lines = read_file()

    busses = lines[1].split(",")
    beginning = 0
    target = {}
    target_tuples = []
    target_tuples_diff = []
    for b in range(len(busses)):
        bus = busses[b]
        if bus != 'x':
            bus = int(bus)
            if beginning == 0:
                beginning = bus

            target[bus] = beginning + b
            target_tuples.append((bus, beginning + b))
            target_tuples_diff.append((bus, b))

    counter = target_tuples[0][1]
    multiple = 1
    keep_going = True
    last_target_timestamp = 0

    while keep_going:
        current_counter = counter * multiple
        for t in range(1, len(target_tuples)):
            ok = True
            if t == 1:
                last_target_timestamp = current_counter

            # print("Comparing " + str(target_tuples[t][0]) + " and " + str(current_counter + target_tuples_diff[t][1]))

            if (current_counter + target_tuples_diff[t][1]) % target_tuples[t][0] != 0:
                ok = False

            if not ok:
                # multiple += 1
                multiple += target_tuples[t][1]
                break

            if ok and t == len(target_tuples) - 1:
                keep_going = False
                break

        print current_counter

    # print counter
    print last_target_timestamp


def yo2():
    # test cases
    lines = "\n7,13,x,x,59,x,31,19".splitlines()
    # lines = "\n17,x,13,19".splitlines()
    # lines = "\n1789,37,47,1889".splitlines()

    lines = read_file()

    busses = lines[1].split(",")
    time = 1
    interval = 1
    for index, bus in enumerate([int(x) if x != 'x' else 1 for x in busses]):
        while True:
            if (time + index) % bus == 0:
                interval *= bus
                break
            time += interval

    print("Answer 2 => " + str(time))


if __name__ == "__main__":
    # yo()
    yo2()
    # yo2_slow()
    #226845233210288

