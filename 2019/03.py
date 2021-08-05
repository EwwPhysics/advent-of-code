with open("input.txt") as inp:
    first, second = [path.split(",") for path in inp.read().splitlines()]


def p1(x, y):
    x = points(x)[0]
    y = points(y)[0]
    intersections = x & y
    return min([abs(a) + abs(b) for a, b in intersections])


def p2(x, y):
    x, x_time = points(x)
    y, y_time = points(y)
    intersections = x & y
    return min([x_time[point] + y_time[point] for point in intersections])


def points(directions):
    x, y = 0, 0
    p = set()
    time = {}
    i = 0
    for line in directions:
        d, length = line[0], int(line[1:])
        if d == "U":
            new = list(zip([x] * (length + 1), range(y + 1, y + length + 1)))
            y += length
        elif d == "D":
            new = list(zip([x] * (length + 1), reversed(range(y - length, y))))
            y -= length
        elif d == "R":
            new = list(zip(range(x + 1, x + length + 1), [y] * (length + 1)))
            x += length
        elif d == "L":
            new = list(zip(reversed(range(x - length, x)), [y] * (length + 1)))
            x -= length
        else:
            raise Exception("hm")
        p.update(new)
        for point, t in zip(new, range(i + 1, i + length + 1)):
            if point not in time:
                time[point] = t
        i += length
    return p, time


print(p1(first, second))
