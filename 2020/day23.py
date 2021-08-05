import time

with open('inputs/input23.txt') as fin:
    a = fin.read()


def part_1(data):
    tic = time.perf_counter()
    data = [int(x) for x in data]
    for i in range(10):
        picked = data[1:4]
        current = data[0]
        del data[1:4]
        below = {x for x in data if x < int(current)}
        if below:
            loc = data.index(max(below))
            data = data[:loc + 1] + picked + data[loc + 1:]
        else:
            loc = data.index(max(data))
            data = data[:loc + 1] + picked + data[loc + 1:]
        data = data[1:] + [data[0]]
    data = data[data.index(1) + 1:] + data[:data.index(1)]
    toc = time.perf_counter()
    return data, toc - tic


def part_2(data):
    d = [int(x) for x in data]
    m = max(d)
    add = [x for x in range(m + 1, 1000001)]
    data = d + add
    for i in range(10000000):
        picked = data[1:4]
        current = data[0]
        data = [data[0]] + data[4:]
        below = [x for x in data if x < int(current)]
        if below:
            loc = data.index(max(below))
            data = data[:loc + 1] + picked + data[loc + 1:]
        else:
            loc = data.index(max(data))
            data = data[:loc + 1] + picked + data[loc + 1:]
        data = data[1:] + [data[0]]
    return data[data.index(1) + 1:data.index(1) + 3]


# print(a)
print(part_1(a))
# 0.00016538499999999012
# 0.00015350999999996784
# print(part_2(a))
