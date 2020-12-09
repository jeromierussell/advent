def read_file():
    with open('./input/advent_day_9_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()
        raw_lines = map(int, raw_lines)

    # print(raw_lines)

    return raw_lines


def meat(lines, index, chunk, target):
    prior = lines[index - chunk: index]

    match = False
    for x in range(chunk):
        for y in range(chunk):
            if x != y:
                if prior[x] + prior[y] == target:
                    match = True

    return match


def meat_2(lines, index, chunk, target):
    prior = lines[index - chunk: index]

    if sum(prior) == target:
        return min(prior), max(prior)

    return None


def yo():
    lines = read_file()

    answer_1 = None

    for i in range(25, len(lines)):
        if not meat(lines, i, 25, int(lines[i])):
            answer_1 = lines[i]
            print("Answer 1 => " + str(answer_1))
            break

    for i in range(2, len(lines)):
        for chunk in range(2, i+1):
            answer_2 = meat_2(lines, i, chunk, answer_1)
            if answer_2:
                print(answer_2)
                print("Answer 2 => " + str(answer_2[0] + answer_2[1]))
                break


if __name__ == "__main__":
    yo()

