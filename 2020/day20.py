import math

with open('inputs/input20.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [x.split('\n') for x in data.split('\n\n')]
    for a, b in enumerate(x):
        x[a] = [int(b[0][5:-1])] + [b[1]] + [b[-1]] + [''.join([i[-1] for i in b[1:]])] + [''.join([i[0] for i in b[1:]])]
    return x


a = parse(raw)
flat = [x for sublist in a for x in sublist if isinstance(x, str)]


def flip(L):
    return [x.reverse() for x in L]


def part_1(data, flat_data):
    corners = []
    for i in range(0, len(flat_data) - 3, 4):
        edge1 = flat_data[i]
        edge2 = flat_data[i + 1]
        edge3 = flat_data[i + 2]
        edge4 = flat_data[i + 3]
        test = edge1[::-1]
        test1 = edge2[::-1]
        test2 = edge3[::-1]
        test3 = edge4[::-1]
        count = (flat_data.count(edge1) + flat_data.count(edge2) + flat_data.count(edge3) + flat_data.count(edge4)
                 + flat_data.count(test) + flat_data.count(test1) + flat_data.count(test2) + flat_data.count(test3))
        if count <= 6:
            loc = i // 4
            corners.append(data[loc])
    return math.prod([x[0] for x in corners])


# print(a)
# print(flat)
# print(len(a))
print(part_1(a, flat))
