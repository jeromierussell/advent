def advent_1():
    # formatted_input = input.split()

    with open('./input/advent_day_1_input.txt', 'r') as the_file:
        formatted_input = the_file.readlines()

    data = []

    for x in formatted_input:
        datum = int(x)
        data.append(datum)

    print(data)

    target = 2020

    x_answer = 0
    y_answer = 0

    for x in data:
        for y in data:
            if x + y == target:
                x_answer = x
                y_answer = y
                break
        else:
            continue

        break

    print(x_answer)
    print(y_answer)
    print("Answer 1 => " + str(x_answer * y_answer))


def advent_2():
    with open('./input/advent_day_1_input.txt', 'r') as the_file:
        formatted_input = the_file.readlines()

    data = []

    for x in formatted_input:
        datum = int(x)
        data.append(datum)

    print(data)

    target = 2020

    y_data = data[:]
    z_data = data[:]

    x_answer = 0
    y_answer = 0
    z_answer = 0

    for x in data:
        for y in y_data:
            for z in z_data:
                if x + y + z == target:
                    x_answer = x
                    y_answer = y
                    z_answer = z
                    break
        else:
            continue

        break

    print(x_answer)
    print(y_answer)
    print(z_answer)
    print("Answer 2 => " + str(x_answer * y_answer * z_answer))


if __name__ == "__main__":
    advent_1()
    advent_2()
