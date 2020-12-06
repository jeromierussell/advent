def narrow(the_min, the_max, step):
    half = (the_max - the_min) / 2 + the_min

    if step == 'F' or step == 'L':
        return_val = the_min, half
    else:
        return_val = half + 1, the_max

    print str(the_min) + " - " + str(the_max) + " (" + step + ") -> " + str(return_val)

    return return_val


def yo():
    with open('./input/advent_day_5_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

    # raw_lines = ['FBFBBFFRLR','BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
    #print(raw_lines)

    seats = set()
    seat_ids = set()

    for line in raw_lines:
        the_min = 0
        the_max = 127
        for row in range(6):
            (the_min, the_max) = narrow(the_min, the_max, line[row])

        if the_min != the_max:
            if line[6] == 'B':
                the_min = the_max

        seat_row = the_min

        the_min = 0
        the_max = 7
        for col in range(7, 10):
            (the_min, the_max) = narrow(the_min, the_max, line[col])

        seat_col = the_min

        seat = seat_row * 8 + seat_col

        print str(seat_row) + ":" + str(seat_col) + " -> " + str(seat)

        seats.add((seat_row, seat_col))
        seat_ids.add(seat)

    seat_min = min(seat_ids)
    answer_1 = max(seat_ids)
    print "\n" + str(answer_1)

    # print str(seats)
    for row in range(1, 127):
        for col in range(0, 8):
            if (row, col) not in seats:
                seat_id = row * 8 + col

                if seat_id not in seat_ids and answer_1 >= seat_id >= seat_min:
                    print "\n" + str(seat_id)


if __name__ == "__main__":
    yo()
