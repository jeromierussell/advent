def yo():
    with open('./input/advent_day_3_input.txt', 'r') as the_file:
        lines = the_file.read().splitlines()

    # print(lines)

    line_length = len(lines[0])
    height = len(lines)

    trees = 0

    x_index = 0
    y_index = 0
    for line in lines:
        x_index += 3
        y_index += 1

        if (y_index >= height):
            print("I'm out")
            break

        if (x_index >= line_length):
            print('wrapping')
            x_index = x_index - line_length

        print(str(y_index) + '-> ' + str(x_index) + ": " + lines[y_index])

        # print(lines[y_index][x_index])

        if (lines[y_index][x_index] == '#'):
            print("hit!")
            trees += 1

    print(trees)

def helper(lines, line_length, height, right, down):
    trees = 0

    x_index = 0
    y_index = 0
    for line in lines:
        x_index += right
        y_index += down

        if (y_index >= height):
            print("I'm out")
            break

        if (x_index >= line_length):
            print('wrapping')
            x_index = x_index - line_length

        print(str(y_index) + '-> ' + str(x_index) + ": " + lines[y_index])

        # print(lines[y_index][x_index])

        if (lines[y_index][x_index] == '#'):
            print("hit!")
            trees += 1

    print(trees)

    return trees

def yo2():
    with open('./input/advent_day_3_input.txt', 'r') as the_file:
        lines = the_file.read().splitlines()

    line_length = len(lines[0])
    height = len(lines)

    try_1 = helper(lines, line_length, height, 1, 1)
    try_2 = helper(lines, line_length, height, 3, 1)
    try_3 = helper(lines, line_length, height, 5, 1)
    try_4 = helper(lines, line_length, height, 7, 1)
    try_5 = helper(lines, line_length, height, 1, 2)

    print("-----------")

    print(try_1)
    print(try_2)
    print(try_3)
    print(try_4)
    print(try_5)

    # print(long(int(try_1) * int(try_2) * int(try_3) * int(try_4) & int(try_5)))
    print(try_1 * try_2 * try_3 * try_4 * try_5)

    # 7812180000


if __name__ == "__main__":
    yo()
