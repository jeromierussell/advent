def yo():
    with open('./input/advent_day_6_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    #    print raw_lines

    entries = []
    entry = []
    for line in raw_lines:
        if line == '':
            entries.append(entry)
            entry = []
        else:
            entry.append(line)

    entries.append(entry)

    # print entries

    total = 0
    for e in entries:
        uniques = set()
        for person in e:
            for answer in person:
                uniques.add(answer)

        # print str(uniques)
        total += len(uniques)

    print total


def yo2():
    with open('./input/advent_day_6_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    #    print raw_lines

    entries = []
    entry = []
    for line in raw_lines:
        if line == '':
            entries.append(entry)
            entry = []
        else:
            entry.append(line)

    entries.append(entry)

    # print entries

    total = 0
    for e in entries:
        group = []
        for person in e:
            uniques = set()
            for answer in person:
                uniques.add(answer)

            group.append(uniques)

        same = set.intersection(*group)
        # print "\n" + str(same)
        total += len(same)

    print total


if __name__ == "__main__":
    yo2()
