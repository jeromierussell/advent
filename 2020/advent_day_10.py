def read_file():
    with open('./input/advent_day_10_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()
        raw_lines = map(int, raw_lines)

    # print(raw_lines)

    return raw_lines


def yo():
    lines = read_file()

    lines.sort()

    # print(lines)

    ones = 1
    threes = 1

    i = 0
    while i < (len(lines) - 1):
        doo_hicky = lines[i]

        diff = lines[i + 1] - doo_hicky

        # print(str(i) + ": " + str(doo_hicky) + ", " + str(lines[i + 1]) + " = " + str(diff))

        if diff > 3:
            print "BARF!"
        elif diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1

        i += 1

    # print(ones, threes)
    print("Answer 1 => " + str(ones * threes))


def yo2_bad():
    lines = read_file()

    lines = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    # lines = [5, 1, 4, 6, 7]

    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    print(lines)

    target = lines[-1]
    print("Target: " + str(target))

    totals = []
    i = 0
    list_len = len(lines)
    paths_to = {}

    while i < list_len:
        doo_hicky = lines[i]

        first = None
        second = None
        third = None

        if i < list_len - 1:
            first = lines[i+1]

        if i < list_len - 2:
            second = lines[i+2]

        if i < list_len - 3:
            third = lines[i+3]

        total_for_i = 0
        if first and first - doo_hicky <= 3:
            paths_to_first = paths_to.get(first, None)
            if not paths_to_first:
                paths_to_first = 0
                paths_to[first] = paths_to_first

            paths_to_first += 1
            paths_to[first] = paths_to_first

        if second and second - doo_hicky <= 3:
            paths_to_second = paths_to.get(second, None)
            if not paths_to_second:
                paths_to_second = 0
                paths_to[second] = paths_to_second

            paths_to_second += 1
            paths_to[second] = paths_to_second

        if third and third - doo_hicky <= 3:
            paths_to_third = paths_to.get(third, None)
            if not paths_to_third:
                paths_to_third = 0
                paths_to[third] = paths_to_third

            paths_to_third += 1
            paths_to[third] = paths_to_third

        # print(str(i) + ": " + str(doo_hicky) + ", " + str(first) + ", " + str(second) + ", " + str(third) + " = " + str(total_for_i) )
        #
        # if total_for_i > 0:
        #     totals.append(total_for_i)

        i += 1

    # total = 1
    # for i in totals:
    #     total *= i


    # print("Answer 2 => " + str(total))
    print("Answer 2 => " + str(paths_to.get(target-1)))

    print("Answer 2 => " + str(paths_to.get(target-2)))

    print("Answer 2 => " + str(paths_to.get(target-3)))

    print("Answer 2 => " + str(paths_to[target]))
    # print(paths_to)


def yo2_bad_2():
    lines = read_file()

    lines = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    lines = [5, 1, 4, 6, 7]

    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    print(lines)

    paths = [[0]]
    # totals = []
    total = 0
    i = 0
    list_len = len(lines)
    target = lines[-1]

    # unique_paths = set()

    while paths:
        path = paths.pop()
        print(path)
        for i in range(len(lines)):

            # total += 1

            doo_hicky = lines[i]
            print(doo_hicky)
            if doo_hicky in path:
                print("continue")
                continue
            else:

                first = None
                second = None
                third = None

                if i < list_len - 1:
                    first = lines[i + 1]

                if i < list_len - 2:
                    second = lines[i + 2]

                if i < list_len - 3:
                    third = lines[i + 3]

                print(str(i) + ": " + str(doo_hicky) + ", " + str(first) + ", " + str(second) + ", " + str(third))

                if first and first - doo_hicky <= 3:
                    new_path = path[:]
                    new_path.append(doo_hicky)
                    new_path.append(first)
                    if first == target:
                        total += 1
                        print(" 1 => " + str(new_path))
                        # unique_paths.add(map(str, new_path))
                    else:
                        paths.append(new_path)

                if second and second - doo_hicky <= 3:
                    new_path = path[:]
                    new_path.append(doo_hicky)
                    new_path.append(second)
                    if second == target:
                        total += 1
                        print(" 2 => " + str(new_path))
                        # unique_paths.add(map(str, new_path))
                    else:
                        paths.append(new_path)

                if third and third - doo_hicky <= 3:
                    new_path = path[:]
                    new_path.append(doo_hicky)
                    new_path.append(third)
                    if third == target:
                        total += 1
                        print(" 3 => " + str(new_path))
                        # unique_paths.add(map(str, new_path))
                    else:
                        paths.append(new_path)

    print("Answer 2 => " + str(total))
    # print("Answer 2 => " + str(len(unique_paths)))


def yo2_bad_3():
    lines = read_file()

    lines = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    lines = [5, 1, 4, 6, 7]

    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    print(lines)

    totals = []
    i = 0
    list_len = len(lines)
    parsed = set()
    three_sets = set()
    while i < list_len:
        doo_hicky = lines[i]

        first = None
        second = None
        third = None

        if i < list_len - 1:
            first = lines[i+1]

        if i < list_len - 2:
            second = lines[i+2]

        if i < list_len - 3:
            third = lines[i+3]

        total_for_i = 0
        if first and first - doo_hicky <= 3:
            first_key = str(doo_hicky) + "-" + str(first)
            if first_key not in parsed:
                parsed.add(first_key)
                print("1 adding " + first_key)
                total_for_i += 1
                # add = True
                # for s in three_sets:
                #     s_range = range(s[0], s[1])
                #     if doo_hicky in s_range and first in s_range:
                #         print(" hit on " + str(s_range) + " ... " + str(doo_hicky) + ", " + str(first))
                #         add = False
                #
                # if add:
                #     print("1 adding " + first_key)
                #     total_for_i += 1

        if second and second - doo_hicky <= 3:
            second_key = str(doo_hicky) + "-" + str(second)
            if second_key not in parsed:
                parsed.add(second_key)
                print("2 adding " + second_key)
                total_for_i += 1
                # add = True
                # for s in three_sets:
                #     s_range = range(s[0], s[1])
                #     if doo_hicky in s_range and second in s_range:
                #         print(" hit on " + str(s_range) + " ... " + str(doo_hicky) + ", " + str(second))
                #         add = False
                #
                # if add:
                #     print("2 adding " + second_key)
                #     total_for_i += 1

        third_key = str(doo_hicky) + "-" + str(third)
        if third and third - doo_hicky <= 3:
            if third_key not in parsed:
                total_for_i += 1
                parsed.add(third_key)
                print("3 adding " + third_key)

        # if total_for_i == 3:
        #     three_sets.add((doo_hicky, third))

        print(str(i) + ": " + str(doo_hicky) + ", " + str(first) + ", " + str(second) + ", " + str(third) + " = " + str(total_for_i) )

        if total_for_i > 0:
            totals.append(total_for_i)

        i += 1

    total = 1
    for i in totals:
        total *= i

    print("Answer 2 => " + str(total))


def yo2_works_but_SLOW():
    lines = read_file()

    # lines = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    # lines = [5, 1, 4, 6, 7]
    # lines = [28, 33, 18, 42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    target = lines[-1]
    print("Target: " + str(target))

    print(lines)

    totals = []
    i = 0
    list_len = len(lines)
    paths = [[0]]
    completed_paths = []
    while paths:
        path = paths.pop()
        # print("current path: " + str(path))

        i = 0
        while i < list_len:
            doo_hicky = lines[i]

            if doo_hicky == target:
                # print(0)
                # completed_paths.append(path)
                i += 1
                break

            if path[-1] == doo_hicky:
                first = None
                second = None
                third = None

                if i < list_len - 1:
                    first = lines[i + 1]

                if i < list_len - 2:
                    second = lines[i + 2]

                if i < list_len - 3:
                    third = lines[i + 3]

                # print(str(i) + ": " + str(doo_hicky) + ", " + str(first) + ", " + str(second) + ", " + str(third))

                if first and first - doo_hicky <= 3:
                    new_path = path[:]
                    new_path.append(first)

                    if first == target:
                        # print(1)
                        completed_paths.append(new_path)
                        print ("New completed paths size " + str(len(completed_paths)))
                    else:
                        # print("first - appending " + str(new_path))
                        paths.append(new_path)

                if second and second - doo_hicky <= 3:
                    new_path = path[:]
                    new_path.append(second)
                    if second == target:
                        # print(2)
                        completed_paths.append(new_path)
                        print ("New completed paths size " + str(len(completed_paths)))
                    else:
                        # print("second - appending " + str(new_path))
                        paths.append(new_path)

                if third and third - doo_hicky <= 3:
                    new_path = path[:]
                    new_path.append(third)
                    if third == target:
                        # print(3)
                        completed_paths.append(new_path)
                        print ("New completed paths size " + str(len(completed_paths)))
                    else:
                        # print("third - appending " + str(new_path))
                        paths.append(new_path)

                break

            i += 1

    # print(completed_paths)
    print("Answer 2 => " + str(len(completed_paths)))


def yo2():
    lines = read_file()

    # lines = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    # lines = [5, 1, 4, 6, 7]
    # lines = [28, 33, 18, 42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    target = lines[-1]
    print("Target: " + str(target))

    print(lines)

    # i = 0
    total = 0
    list_len = len(lines)
    paths = [[0]]
    completed_paths = []
    while paths:
        path = paths.pop()
        # print("current path: " + str(path))

        doo_hicky = path[-1]
        i = lines.index(doo_hicky)

        if doo_hicky == target:
            # print(0)
            # completed_paths.append(path)
            break

        first = None
        second = None
        third = None

        if i < list_len - 1:
            first = lines[i + 1]

        if i < list_len - 2:
            second = lines[i + 2]

        if i < list_len - 3:
            third = lines[i + 3]

        # print(str(i) + ": " + str(doo_hicky) + ", " + str(first) + ", " + str(second) + ", " + str(third))

        if first and first - doo_hicky <= 3:
            new_path = path[:]
            new_path.append(first)

            if first == target:
                # print(1)
                # completed_paths.append(new_path)
                total += 1
                # print ("New completed paths size " + str(len(completed_paths)))
            else:
                # print("first - appending " + str(new_path))
                paths.append(new_path)

        if second and second - doo_hicky <= 3:
            new_path = path[:]
            new_path.append(second)
            if second == target:
                # print(2)
                # completed_paths.append(new_path)
                total += 1
                # print ("New completed paths size " + str(len(completed_paths)))
            else:
                # print("second - appending " + str(new_path))
                paths.append(new_path)

        if third and third - doo_hicky <= 3:
            new_path = path[:]
            new_path.append(third)
            if third == target:
                # print(3)
                # completed_paths.append(new_path)
                total += 1
                # print ("New completed paths size " + str(len(completed_paths)))
            else:
                # print("third - appending " + str(new_path))
                paths.append(new_path)

        if total > 0 and total % 10000 == 0:
            print(total)

    # print(completed_paths)
    # print("Answer 2 => " + str(len(completed_paths)))
    print("Answer 2 => " + str(total))


# TODO JRO - i have to come up w/ a faster solution. The logic is right in mine but too complex & slow.
# Come back and understand why my 5000 attempts failed when this is so easy

def yo_copied():
    lines = read_file()

    # lines = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    # lines = [5, 1, 4, 6, 7]
    # lines = [28, 33, 18, 42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

    # lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    # del lines[-1]  # Remove 0 from output options
    adapter_paths = {}
    adapter_paths[0] = 1
    for adapter in lines:
        paths_to = 0
        for n in (1, 2, 3):
            paths_to += adapter_paths.get(adapter - n, 0)
        adapter_paths[adapter] = paths_to

    print("Answer 2 => " + str(adapter_paths[lines[-1]]))


if __name__ == "__main__":
    # yo2()
    # 6044831973376
    # 6,044,831,973,376

    yo()
    yo_copied()

