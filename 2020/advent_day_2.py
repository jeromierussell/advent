def yo():
    r = []

    with open('./input/advent_day_2_input.txt', 'r') as the_file:
        lines = the_file.readlines()

    # print(lines)

    for i in lines:
        line = i.split(' ')
        # print(line)
        r.append({'min_max': line[0], 'letter': line[1][0], 'strang': line[2] })

    # print(r)
    answer = 0

    for line in r:
        min_max = line['min_max'].split('-')
        the_min = int(min_max[0])
        the_max = int(min_max[1])

        letter = line['letter']
        strang = line['strang']

        o = strang.count(letter)

        if the_min <= o <= the_max:
            # print(strang + ": " + str(o) + " " + letter + " " + min_max[0] + "-" + min_max[1])
            answer += 1
        else:
            pass
            # print(strang + ": " + str(o) + " " + letter + " " + min_max[0] + "-" + min_max[1])

    print("Answer 1 => " + str(answer))


def yo2():
    r = []

    with open('./input/advent_day_2_input.txt', 'r') as the_file:
        lines = the_file.readlines()

    # print(lines)

    for i in lines:
        line = i.split(' ')
        # print(line)
        r.append({'min_max': line[0], 'letter': line[1][0], 'strang': line[2] })

    # print(r)
    answer = 0

    for line in r:
        min_max = line['min_max'].split('-')
        the_min = int(min_max[0])
        the_max = int(min_max[1])

        letter = line['letter']
        strang = line['strang']

        if (strang[the_min-1] == letter and strang[the_max-1] != letter) or (strang[the_min-1] != letter and strang[the_max-1] == letter):
            # print(strang + ": " + letter + " " + min_max[0] + "-" + min_max[1])
            answer += 1
        else:
            pass
            # print('wrong ->' + strang + ": " + letter + " " + min_max[0] + "-" + min_max[1])

    print("Answer 2 => " + str(answer))


if __name__ == "__main__":
    yo()
    yo2()
