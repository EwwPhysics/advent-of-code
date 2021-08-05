with open('inputs/input9.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [int(x) for x in data.split('\n')]
    return x


a = parse(raw)


def part_1(data):
    preamble = [x for x in data[:25]]
    for x in data[25:]:
        nums = {i for i in preamble if x - i in preamble}
        if len(nums) == 0:
            return x
        preamble.pop(0)
        preamble.append(x)


def part_2(data, value):
    loc = data.index(value)
    for i, x in enumerate(data[:loc]):
        a = i
        while a < loc:
            test = [num for num in data[i:(a + 1)]]
            if sum(test) == value:
                return min(test) + max(test)
            a += 1


x = part_1(a)
print(x)
print(part_2(a, x))
