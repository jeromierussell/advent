def yo():
    with open('./input/advent_day_8_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

        # print raw_lines

    accumulator = 0
    visited = set()
    current_location = 0
    keep_playing = True
    while keep_playing:
        line = raw_lines[current_location].split(' ')
        action = line[0]

        # print(line)

        direction = line[1][0]
        value = int(line[1][1:len(line[1])])

        # print(action + " " + direction + " " + value)

        if current_location in visited:
            print("Answer 1 => " + str(accumulator))
            keep_playing = False
            break

        visited.add(current_location)

        if action == 'jmp':
            if direction == '-':
                current_location -= value
            else:
                current_location += value
        else:
            current_location += 1

            if action == 'acc':
                if direction == '-':
                    accumulator -= value
                else:
                    accumulator += value


def yo2():
    with open('./input/advent_day_8_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

        # print raw_lines

    accumulator = 0
    visited = set()
    current_location = 0
    keep_playing = True

    tried = set()

    # print("length [" + str(len(raw_lines)) + "]")

    current_try = False
    iteration = 0

    raw_copy = raw_lines[:]

    while keep_playing:
        # print(current_location)
        # print(raw_lines[current_location].split(' '))

        if int(current_location) >= (len(raw_lines) - 1):
            keep_playing = False
            break

        if current_location in visited:
            # print("resetting...")
            current_try = False
            current_location = 0
            iteration += 1
            raw_copy = raw_lines[:]
            visited = set()
            accumulator = 0
            # print(iteration)

        line = raw_copy[current_location]
        if not current_try and current_location not in tried:
            # print(current_location)
            # print('yo')
            if 'nop' in line:
                # print('yo1')
                raw_copy[current_location] = raw_copy[current_location].replace('nop', 'jmp')
                tried.add(current_location)
                current_try = True
            elif 'jmp' in line:
                # print('yo2')
                raw_copy[current_location] = raw_copy[current_location].replace('jmp', 'nop')
                tried.add(current_location)
                current_try = True

        # if current_location in visited:

        line = raw_copy[current_location].split(' ')
        # print(line)
        # print(current_location)

        action = line[0]

        # print(line)

        direction = line[1][0]
        value = int(line[1][1:len(line[1])])

        # print(action + " " + direction + " " + value)

        visited.add(current_location)

        if action == 'jmp':
            if direction == '-':
                current_location -= value
            else:
                current_location += value
                # print("jumping " + str(value))
        else:
            current_location += 1

            if action == 'acc':
                if direction == '-':
                    accumulator -= value
                else:
                    accumulator += value

        # print(current_location)

    print("Answer 2 => " + str(accumulator))


if __name__ == "__main__":
    yo()
    yo2()
