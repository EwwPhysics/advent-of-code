with open('inputs/input.txt') as fin:
    puzzleinput = fin.read()


def parse(data):
    x = [int(x) for x in data.split('\n')]
    return x


a = parse(puzzleinput)


def part_1(L):
    for x in L:
        diff = 2020 - x
        if diff in L:
            return diff * x


print(part_1(a))


def part_2(L):
    for x in L:
        diff = 2020 - x
        for y in L:
            diffA = diff - y
            if diffA in L:
                return diffA * y * x


print(part_2(a))
