from copy import deepcopy


def read_file():
    with open('./input/advent_day_11_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    data = []
    for line in raw_lines:
        line_x = []
        for x in line:
            line_x.append(x)

        data.append(line_x)

    return data

"""
1 2 3
8 X 4
7 6 5
"""
def num_adjacent_occupied(x, y, data, line_length, graph_length):
    # print("called - row [" + str(y) + "] col [" + str(x))

    count = 0

    # 1
    if y > 0 and x > 0 and data[y - 1][x - 1] == '#':
        count += 1

    # 2
    if y > 0 and data[y - 1][x] == '#':
        count += 1

    # 3
    if y > 0 and x < line_length - 1 and data[y - 1][x + 1] == '#':
        count += 1

    # 4
    if x < line_length - 1 and data[y][x + 1] == '#':
        count += 1

    # 5
    if y < graph_length - 1 and x < line_length - 1 and data[y + 1][x + 1] == '#':
        count += 1

    # 6
    if y < graph_length - 1 and data[y + 1][x] == '#':
        count += 1

    # 7
    if y < graph_length - 1 and x > 0 and data[y + 1][x - 1] == '#':
        count += 1

    # 8
    if x > 0 and data[y][x - 1] == '#':
        count += 1

    return count

"""
1 2 3
8 X 4
7 6 5
"""
# y == 0, x == 3
def num_adjacent_occupied2(x, y, data, line_length, graph_length):
    # print("called - row [" + str(y) + "] col [" +  + "]")

    original_x = x
    original_y = y

    count = 0

    # 1
    while y > 0 and x > 0:
        if data[y - 1][x - 1] == 'L':
            break

        if data[y - 1][x - 1] == '#':
            count += 1
            break

        y -= 1
        x -= 1

    x = original_x
    y = original_y

    # 2
    while y > 0:
        if data[y - 1][x] == 'L':
            break

        if data[y - 1][x] == '#':
            count += 1
            break

        y -= 1

    x = original_x
    y = original_y

    # 3
    while y > 0 and x < line_length - 1:
        if data[y - 1][x + 1] == 'L':
            break

        if data[y - 1][x + 1] == '#':
            count += 1
            break

        y -= 1
        x += 1

    x = original_x
    y = original_y

    # 4
    while x < line_length - 1:
        if data[y][x + 1] == 'L':
            break

        if data[y][x + 1] == '#':
            count += 1
            break

        x += 1

    x = original_x
    y = original_y

    # 5
    while y < graph_length - 1 and x < line_length - 1:
        if data[y + 1][x + 1] == 'L':
            break

        if data[y + 1][x + 1] == '#':
            count += 1
            break

        y += 1
        x += 1

    x = original_x
    y = original_y

    # 6
    while y < graph_length - 1:
        if data[y + 1][x] == 'L':
            break

        if data[y + 1][x] == '#':
            count += 1
            break

        y += 1

    x = original_x
    y = original_y

    # 7
    while y < graph_length - 1 and x > 0:
        if data[y + 1][x - 1] == 'L':
            break

        if data[y + 1][x - 1] == '#':
            count += 1
            break

        x -= 1
        y += 1

    x = original_x
    y = original_y

    # 8
    while x > 0:
        if data[y][x - 1] == 'L':
            break

        if data[y][x - 1] == '#':
            count += 1
            break

        x -= 1

    return count


def print_graph(data):
    for y in data:
        line = ''
        for x in y:
            line += x
        print line


def count_occupied(data, graph_length, line_length):
    count = 0
    for y in range(graph_length):
        for x in range(line_length):
            if data[y][x] == '#':
                count += 1

    return count


def iteration(data, line_length, graph_length):
    new_data = deepcopy(data)

    num_moves = 0
    for y in range(len(data)):
        for x in range(line_length):
            if data[y][x] == 'L':
                adjacent_occupied = num_adjacent_occupied(x, y, data, line_length, graph_length)
                # print("row [" + str(y) + "] col [" + str(x) + "] == [" + str(adjacent_occupied) + "]")
                if adjacent_occupied == 0:
                    new_data[y][x] = '#'
                    num_moves += 1
            elif data[y][x] == '.':
                pass
            else: #
                adjacent_occupied = num_adjacent_occupied(x, y, data, line_length, graph_length)
                # print("row [" + str(y) + "] col [" + str(x) + "] == [" + str(adjacent_occupied) + "]")
                if adjacent_occupied >= 4:
                    new_data[y][x] = 'L'
                    num_moves += 1

    return new_data, num_moves


def iteration2(data, line_length, graph_length):
    new_data = deepcopy(data)

    num_moves = 0
    for y in range(len(data)):
        for x in range(line_length):
            if data[y][x] == 'L':
                adjacent_occupied = num_adjacent_occupied2(x, y, data, line_length, graph_length)
                # print("row [" + str(y) + "] col [" + str(x) + "] == [" + str(adjacent_occupied) + "]")
                if adjacent_occupied == 0:
                    new_data[y][x] = '#'
                    num_moves += 1
            elif data[y][x] == '.':
                pass
            else: #
                adjacent_occupied = num_adjacent_occupied2(x, y, data, line_length, graph_length)
                # print("row [" + str(y) + "] col [" + str(x) + "] == [" + str(adjacent_occupied) + "]")
                if adjacent_occupied >= 5:
                    new_data[y][x] = 'L'
                    num_moves += 1

    return new_data, num_moves


def yo():
    data = read_file()

    # print_graph(data)

    line_length = len(data[0])
    graph_length = len(data)

    num_moves = 1
    new_data = data
    while num_moves > 0:
        new_data, num_moves = iteration(new_data, line_length, graph_length)
        # print
        # print_graph(new_data)

    print("Answer 1 => " + str(count_occupied(new_data, graph_length, line_length)))


def yo2():
    data = read_file()

    # print_graph(data)

    line_length = len(data[0])
    graph_length = len(data)

    num_moves = 1
    new_data = data
    while num_moves > 0:
        new_data, num_moves = iteration2(new_data, line_length, graph_length)
        # print
        # print_graph(new_data)

    print("Answer 2 => " + str(count_occupied(new_data, graph_length, line_length)))


if __name__ == "__main__":
    yo()
    yo2()
