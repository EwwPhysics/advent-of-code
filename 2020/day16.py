from itertools import chain

with open('inputs/input16.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [x for x in data.split('\n')]
    x[:x.index('')] = [i.split(':')[1][1:] for i in x[:x.index('')]]
    ranges = x[:x.index('')]
    for a, b in enumerate(ranges):
        ranges[a] = b.split(' or ')
        ranges[a] = [i.split('-') for i in ranges[a]]
        ranges[a] = [int(item) for sublist in ranges[a] for item in sublist]
    x[:x.index('')] = ranges
    near = [i.split(',') for i in x[(x.index('nearby tickets:') + 1):]]
    for a, b in enumerate(near):
        for i, n in enumerate(b):
            near[a][i] = int(n)
    x[x.index('nearby tickets:') + 1:] = near
    return x


a = parse(raw)


def part_1(data):
    v = set()
    for a, b, c, d in data[:data.index('')]:
        v.update(list(chain(range(a, b + 1), range(c, d + 1))))
    near = data[(data.index('nearby tickets:') + 1):]
    valid = [ticket for ticket in near if len(set(ticket).intersection(v)) == len(set(ticket))]
    near = [item for sublist in near for item in sublist if item not in v]
    return sum(near), valid


def part_2(data, near, raw_data):
    r = {}
    raw_data = [x for x in raw_data.split('\n')]
    fields = [i.split(':')[0] for i in raw_data[:6]]
    for i, x in enumerate(fields):
        r[x] = set(list(chain(range(data[i][0], data[i][1]), range(data[i][2], data[i][3]))))
    near = [list(row) for row in zip(*near)]
    counts = []
    for a, b in enumerate(near):
        count = 0
        for key, value in r:
            if len(set(b) | value) == len(set(b)):
                count += 1
        counts.append(count)
    print(r)
    return counts


# print(a[:6])
print(part_1(a)[0])
print(part_2(a, part_1(a)[1], raw))
