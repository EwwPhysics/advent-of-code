with open('inputs/input7.txt') as fin:
    raw = fin.read()


def parse(data):
    a = [x for x in data.split('\n')]
    for i, x in enumerate(a):
        split = x.split()
        a[i] = [split[:2]] + [[split[b], f'{split[b + 1]} {split[b + 2]}'] for b in range(4, len(split) - 3, 4)]
    return a


data = parse(raw)


def part_1(data):
    count = 0
    contains = set()
    for a in data:
        for i, x in a:
            if x == 'shiny gold':
                count += 1
                contains.add(f'{a[0][0]} {a[0][1]}')
    before = 0
    after = len(contains)
    while after > before:
        before = len(contains)
        for a in data:
            for i, x in a:
                if x in contains:
                    count += 1
                    contains.add(f'{a[0][0]} {a[0][1]}')
        after = len(contains)
    return len(contains)


print(part_1(data))


def part_2(data, find):
    product = 1
    if len(data) == 0:
        return data
    else:
        location = [i for i, loc in enumerate(data) if find in loc]
        for i, x in enumerate(data[location[0]][1:]):
            product += int(x[0]) * part_2(data, x[1].split())
        return product


print(part_2(data, ['shiny', 'gold']) - 1)
