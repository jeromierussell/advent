def navigate(graph, start, end, path=[]):
    """
    I did cheat a little on this. I knew I needed to navigate a graph and instead of writing this on my own, I borrowed
    and modified an algorithm. More concerned about solving the problem than perfecting logic to navigate the graph. I'm
    # ok with this.
    """
    path = path + [start]
    if start == end:
        return path

    if not graph.get(start):
        return None

    for node in graph[start]:
        if node not in path:
            new_path = navigate(graph, node, end, path)
            if new_path:
                return new_path

    return None


def yo():
    with open('./input/advent_day_7_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

        # print raw_lines

    target = "shiny gold"
    can_hold_shiny_gold_directly = set()

    master_map = {}

    for raw_line in raw_lines:
        line = raw_line.split('contain')

        # 6 is len(" bags ")
        key = line[0][0: len(line[0]) - 6]
        # print("Key [" + key + "]")

        bags_in_bags = line[1].split(',')

        # print(bags_in_bags)

        for b in bags_in_bags:
            words = b.split(' ')
            inner_bag = words[2] + " " + words[3]
            # handle no bags
            if inner_bag != 'other bags.':
                if not master_map.get(key):
                    master_map[key] = []

                master_map[key].append(inner_bag)

                if inner_bag == target:
                    can_hold_shiny_gold_directly.add(key)

    # print(master_map)

    can_hold_shiny_gold = set()
    for key in master_map.keys():
        if key != target:
            ok = navigate(master_map, key, target)
            if ok:
                can_hold_shiny_gold.add(key)

    # print(can_hold_shiny_gold)

    print("Answer 1 => " + str(len(can_hold_shiny_gold)))


def yo2():
    with open('./input/advent_day_7_input.txt', 'r') as the_file:
        raw_lines = the_file.read().splitlines()

        # print raw_lines

    master_map = {}
    master_map_with_counts = {}
    total_bags = 0

    for raw_line in raw_lines:
        line = raw_line.split('contain')

        # 6 is len(" bags ")
        key = line[0][0: len(line[0]) - 6]
        # print("Key [" + key + "]")

        bags_in_bags = line[1].split(',')

        # print(bags_in_bags)

        for b in bags_in_bags:
            words = b.split(' ')
            # print(words)
            inner_bag = words[2] + " " + words[3]
            inner_bag_count = words[1]

            # handle no bags
            if inner_bag != 'other bags.':
                if not master_map.get(key):
                    master_map[key] = []

                if not master_map_with_counts.get(key):
                    master_map_with_counts[key] = []

                master_map[key].append(inner_bag)
                master_map_with_counts[key].append({'bag': inner_bag, 'count': inner_bag_count})

        # print(master_map_with_counts)

    shiny_gold = master_map_with_counts.get("shiny gold")
    print(shiny_gold)

    # BAH - ended up getting help. booooooooo. just didn't have the brain power today to figure out using a stack.
    # tried recursion and struggled. didn't just copy/paste, but did get an idea of using a stack to figure it out

    bags = [('shiny gold', 1)]
    while bags:
        current, count = bags.pop()

        current_contents = master_map_with_counts.get(current)
        if current_contents:
            for content in current_contents:
                color, color_count = content.get('bag'), int(content.get('count'))
                total_count_for_color = int(color_count * count)
                total_bags += total_count_for_color
                bags.append((color, total_count_for_color))

    print("Answer 2 => " + str(total_bags))


if __name__ == "__main__":
    yo()
    yo2()
