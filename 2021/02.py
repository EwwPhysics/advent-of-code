with open("input.txt") as fin:
    data = [x.split() for x in fin.read().splitlines()]


def p1(file):
    f = d = 0
    for a, b in file:
        b = int(b)
        if a == "forward":
            f += b
        elif a == "up":
            d -= b
        else:
            d += b

    return f * d


def p2(file):
    f = d = aim = 0

    for a, b in file:
        b = int(b)

        if a == "forward":
            f += b
            d += aim * b
        elif a == "down":
            aim += b
        else:
            aim -= b

    return f * d


print(p1(data))
print(p2(data))
