def yo(target):
    # starting_data = "0,3,6".split(',')
    # starting_data = "1,3,2".split(',')
    # starting_data = "2,1,3".split(',')
    # starting_data = "2,3,1".split(',')
    # starting_data = "3,2,1".split(',')
    # starting_data = "3,1,2".split(',')
    starting_data = "0,13,1,8,6,15".split(',')

    # moves = []
    last_move = None
    visited = {}
    for i in range(target):
        if i < len(starting_data):
            # moves.append(int(starting_data[i]))
            last_move = int(starting_data[i])
            visited[int(starting_data[i])] = [i]
        else:
            previous_visited = visited.get(last_move)
            # print "[" + str(i) + "] previous move: " + str(previous_move) + " ... previous visited " + str(previous_visited)
            if previous_visited and len(previous_visited) > 1:
                current_move = previous_visited[-1] - previous_visited[-2]
                # print "new current move == " + str(current_move)
            else:
                current_move = 0
                # print "new current move == 0"

            last_move = current_move
            # moves.append(current_move)

            if visited.get(current_move):
                visited[current_move].append(i)
            else:
                visited[current_move] = [i]

            # if len(visited.get(current_move)) > 2:
            #     visited[current_move] = visited[current_move][-2:]

    # print len(moves)
    # print moves
    print ("Answer [" + str(target) + "] => " + str(last_move))


if __name__ == "__main__":
    yo(2020)
    yo(30000000)
