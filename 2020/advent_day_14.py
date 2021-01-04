import re
from itertools import product


def read_file():
    with open('./input/advent_day_14_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    return raw_lines


def yo():
    """
    mem = {}
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    mem[8] = do_it(11, mask)
    mem[7] = do_it(101, mask)
    mem[8] = do_it(0, mask)

    total = 0
    for item in mem.items():
        total += item[1]

    print total
"""
    mask = None
    mem = {}
    lines = read_file()
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' ')[-1]
            # print mask
        else:
            parsed_line = line.split(' ')
            value = parsed_line[-1]
            key = re.search('(?<=\[).+?(?=\])', parsed_line[0]).group(0)

            # print key, value

            mem[key] = int(value)

            result = do_it(mem[key], mask)
            mem[key] = result
            # print result

    total = 0
    for item in mem.items():
        total += item[1]

    print "Answer 1 => " + str(total)


def do_it(value, mask):
    str_value = list("{0:b}".format(value).zfill(36))
    # print str_value
    for i in range(len(mask)):
        if mask[i] != 'X':
            # print str_value[i], mask[i], int(str_value[i]) ^ int(mask[i])
            # str_value[i] = str(int(str_value[i]) ^ int(mask[i]))
            str_value[i] = mask[i]
    new_str = "".join(str_value)
    # print(new_str)
    # print int(new_str, 2)

    return int(new_str, 2)


def yo_2_slow():
    mask = None
    mem = {}
    lines = """mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1""".splitlines()

    lines = """mask = 00110X11X0000110X0000001000111010X00
mem[39993] = 276
mem[23021] = 365
mem[59102] = 45645
mem[30606] = 2523
mem[38004] = 4503
mem[47790] = 1221939
mem[24194] = 3417""".splitlines()

    lines = read_file()

    for line in lines:
        print(line)

        if line.startswith('mask'):
            mask = line.split(' ')[-1]
        else:
            parsed_line = line.split(' ')
            value = parsed_line[-1]
            key = re.search('(?<=\[).+?(?=\])', parsed_line[0]).group(0)

            # mem[key] = int(value)

            result = do_it_2_slow(int(key), mask)
            for r in result:
                mem[str(r)] = int(value)

    total = 0
    for item in mem.items():
        total += item[1]

    print total


def do_it_2_slow(value, mask):
    # print value
    str_value = list("{0:b}".format(value).zfill(36))
    # print str_value
    for i in range(len(mask)):
        if mask[i] != '0':
            str_value[i] = mask[i]

    new_str = "".join(str_value)

    # print new_str

    # now have to handle all the possible combinations for X
    result_list = set()
    evaluate_me = [str_value]
    while evaluate_me:
        # print(len(evaluate_me))
        str_value = evaluate_me.pop()
        # print("evaluating " + str(str_value))
        has_x = False
        for i in range(len(str_value)):
            if str_value[i] == 'X':
                for x in (0, 1):
                    copy = str_value[:]
                    copy[i] = str(x)

                    evaluate_me.append(copy)

                    has_x = True

        if not has_x:
            result_list.add(int("".join(str_value), 2))

    print result_list

    return result_list



def yo_2():
    mask = None
    mem = {}
    lines = """mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1""".splitlines()


    lines = read_file()

    for line in lines:
        print(line)

        if line.startswith('mask'):
            mask = line.split(' ')[-1]
        else:
            parsed_line = line.split(' ')
            value = parsed_line[-1]
            key = re.search('(?<=\[).+?(?=\])', parsed_line[0]).group(0)

            str_value = list("{0:b}".format(int(key)).zfill(36))
            # print str_value
            for i in range(len(mask)):
                if mask[i] != '0':
                    str_value[i] = mask[i]

            # now have to handle all the possible combinations for X
            # result_list = set()
            evaluate_me = [str_value]
            while evaluate_me:
                # print(len(evaluate_me))
                str_value = evaluate_me.pop()
                # print("evaluating " + str(str_value))
                has_x = False
                for i in range(len(str_value)):
                    if str_value[i] == 'X':
                        for x in (0, 1):
                            copy = str_value[:]
                            copy[i] = str(x)

                            evaluate_me.append(copy)

                            has_x = True

                if not has_x:
                    mem[str(int("".join(str_value), 2))] = int(value)

            # mem[key] = int(value)

            # result = do_it_2(int(key), mask)
            # for r in result:
            #     mem[str(r)] = int(value)

    total = 0
    for item in mem.items():
        total += item[1]

    print total

"""
Running out of time...my solution had good logic, but wouldn't perform. I copied this below to get an answer to
compare to & see how a good performing solution should behave. Below is NOT my work.
"""
def good_2():
    with open('./input/advent_day_14_input.txt', 'r') as f:
        rows = [row.strip() for row in f.readlines()]

    instructions = []
    instruction_regex = re.compile('mem\[(\d*)\]\s=\s(\d*)')
    for row in rows:
        if row.startswith('mask'):
            instructions.append(row.split()[2])
        else:
            mem, value = instruction_regex.findall(row)[0]
            instructions.append((mem, value))
            memory = {}

    for instruction in instructions:
        if type(instruction) is str:
            mask = instruction
        else:
            mem, value = instruction
            mem = format(int(mem), '036b')
            masked_mem = ''
            for index, bit in enumerate(mask):
                if bit == '0':
                    masked_mem += mem[index]
                else:
                    masked_mem += bit

            x_count = masked_mem.count('X')
            for floats in product(('0', '1'), repeat=x_count):
                float_mem = ''
                float_index = 0
                for bit in masked_mem:
                    if bit == 'X':
                        float_mem += floats[float_index]
                        float_index += 1
                    else:
                        float_mem += bit

                memory[int(float_mem, 2)] = int(value)

    # Answer Two
    print("Answer 2 => ", sum(memory.values()))



if __name__ == "__main__":
    yo()
    good_2()

"""
set(['000000000000000000000000000000011011', 
'000000000000000000000000000000011010', 
'000000000000000000000000000000111010', 
'000000000000000000000000000000111011'])
"""