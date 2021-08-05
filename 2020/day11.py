with open('inputs/input11.txt') as fin:
    raw = fin.read()


def parse(raw):
    x = tuple(x for x in raw.split('\n'))
    return x


a = parse(raw)

def part_1(data):
    test = data[:]
    test2 = []
    while test != test2:
        test = data[:]
        for i, x in enumerate(data):
            for a, b in enumerate(x):
                adjacent = [x[a + 1], x[a - 1], data[i + 1][a], data[i + 1][a + 1], data[i + 1][a - 1], data[i -1][a], data[i -1][a + 1], data[i -1][a - 1]]
                if b == 'L' and '#' not in adjacent:

                    data = data[i][:a] + ('#',) + data[i][a:]
                elif b == '#' and adjacent.count('#') >= 4:
                    data = x[:a] + ('L',) + x[a:]
        test2 = data[:]
    return data.count('#')


print(part_1(a))
