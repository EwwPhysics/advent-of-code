import numpy as np

with open('inputs/input17.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [x for x in data.split('\n')]
    return x


a = parse(raw)


def part_1(data):
    b = np.array(data)
    return b



print(a, '\n\n')
print(part_1(a))
