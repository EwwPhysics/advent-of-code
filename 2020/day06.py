with open('inputs/input6.txt') as fin:
    raw = fin.read()


def parse(data):
    return [x.replace('\n', '') for x in data.split('\n\n')]


def parse2(data):
    return [x.splitlines() for x in data.split('\n\n')]


forms = parse(raw)
forms2 = parse2(raw)


def part_1(groups):
    return sum([len(set(x)) for x in groups])


def part_2(groups):
    return sum([len(set.intersection(*[set(i) for i in x])) for x in groups])


print(part_1(forms))

print(part_2(forms2))
