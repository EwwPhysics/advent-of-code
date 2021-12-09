with open("input.txt") as f:
    data = list(map(int, f.read().splitlines()))


def p1(data):
    return sum(b > a for a, b in zip(data, data[1:]))


def p2(data):
    return sum(b > a for a, b in zip(data, data[3:]))


print(p1(data))
print(p2(data))
