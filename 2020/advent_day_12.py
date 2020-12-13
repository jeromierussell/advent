"""
probably my best solution so far...at least since early on
"""


def read_file():
    with open('./input/advent_day_12_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    return raw_lines


def get_new_heading(current_heading, degrees, direction):
    headings = ['N', 'E', 'S', 'W', 'N', 'E', 'S']
    if direction == 'L':
        headings = headings[::-1]

    index = headings.index(current_heading)

    if degrees == 90:
        return headings[index + 1]
    elif degrees == 180:
        return headings[index + 2]
    elif degrees == 270:
        return headings[index + 3]


def get_new_heading2(north, east, direction, degrees):
    west = -1 * east
    south = -1 * north
    if direction == 'R':
        if degrees == 90:
            return west, north
        elif degrees == 180:
            return south, west
        elif degrees == 270:
            return east, south
    else:
        if degrees == 90:
            return east, south
        elif degrees == 180:
            return south, west
        elif degrees == 270:
            return west, north


def yo():
    # test
    lines = """F10
    N3
    F7
    R90
    F11""".splitlines()

    lines = read_file()

    current_north = 0
    current_east = 0
    current_heading = 'E'

    for line in lines:
        # print(line)
        order = line[0]
        moves = int(line[1:])

        if order == 'F':
            order = current_heading

        if order == 'N':
            current_north += moves
        elif order == 'S':
            current_north -= moves
        elif order == 'E':
            current_east += moves
        elif order == 'W':
            current_east -= moves
        elif order == 'R' or order == 'L':
            current_heading = get_new_heading(current_heading, moves, order)

        # print(order, moves, current_heading, current_north, current_east)

    print("Answer 1 => " + str(abs(current_north) + abs(current_east)))


def yo2():
    # test
    lines = """F10
N3
F7
R90
F11""".splitlines()

    lines = read_file()

    current_ship_north = 0
    current_ship_east = 0
    current_waypoint_north = 1
    current_waypoint_east = 10

    for line in lines:
        # print(line)
        order = line[0]
        moves = int(line[1:])

        if order == 'F':
            current_ship_north += (current_waypoint_north * moves)
            current_ship_east += (current_waypoint_east * moves)

        if order == 'N':
            current_waypoint_north += moves
        elif order == 'S':
            current_waypoint_north -= moves
        elif order == 'E':
            current_waypoint_east += moves
        elif order == 'W':
            current_waypoint_east -= moves
        elif order == 'R' or order == 'L':
            (current_waypoint_north, current_waypoint_east) = get_new_heading2(current_waypoint_north, current_waypoint_east, order, moves)

        # print(order, moves, current_heading, current_north, current_east)

    print("Answer 2 => " + str(abs(current_ship_north) + abs(current_ship_east)))


if __name__ == "__main__":
    yo()
    yo2()

