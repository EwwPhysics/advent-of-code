with open('inputs/input12.txt') as fin:
    raw = fin.read()


def parse(raw):
    x = [[x[0], int(x[1:])] for x in raw.split('\n')]
    return x


a = parse(raw)


def part_1(data):
    north = [x[1] if x[0] == 'N' else -(x[1]) if x[0] == 'S' else 0 for x in data]
    east = [x[1] if x[0] == 'E' else -(x[1]) if x[0] == 'W' else 0 for x in data]
    n_s = sum(north)
    e_w = sum(east)
    direction = 1
    for x in data:
        if x[0] == 'L':
            direction -= x[1] // 90
            direction = direction % 4
        elif x[0] == 'R':
            direction += x[1] // 90
            direction = direction % 4
        elif x[0] == 'F':
            if direction == 0:
                n_s += x[1]
            elif direction == 1:
                e_w += x[1]
            elif direction == 2:
                n_s -= x[1]
            elif direction == 3:
                e_w -= x[1]
    return abs(n_s) + abs(e_w)


def part_2(data):
    way = [10, 1, 0]
    n_s = 0
    e_w = 0
    for x in data:
        if way[2] == 0:
            if way[0] < 0:
                way[0] = -way[0]
            if way[1] < 0:
                way[1] = -way[1]
        elif way[2] == 1:
            if way[0] > 0:
                way[0] = -way[0]
            if way[1] < 0:
                way[1] = -way[1]
        elif way[2] == 2:
            if way[0] > 0:
                way[0] = -way[0]
            if way[1] > 0:
                way[1] = -way[1]
        elif way[2] == 3:
            if way[0] < 0:
                way[0] = -way[0]
            if way[1] > 0:
                way[1] = -way[1]
        print(way)
        if x[0] == 'N':
            way[1] += x[1]
        elif x[0] == 'S':
            way[1] -= x[1]
        elif x[0] == 'E':
            way[0] += x[1]
        elif x[0] == 'W':
            way[0] -= x[1]
        elif x[0] == 'R':
            way[2] = (way[2] + (x[1] // 90)) % 4
            num = way[1]
            way[1] = way[0]
            way[0] = num
        elif x[0] == 'L':
            way[2] = (way[2] - (x[1] // 90)) % 4
            num = way[1]
            way[1] = way[0]
            way[0] = num
        elif x[0] == 'F':
            n_s += way[1] * x[1]
            e_w += way[0] * x[1]
            print(n_s, e_w)
    return abs(n_s) + abs(e_w)

print(part_2(a))
