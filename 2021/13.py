with open("input.txt") as fin:
    points, folds = [x.splitlines() for x in fin.read().split("\n\n")]
    points = [tuple(int(x) for x in line.split(",")) for line in points]
    folds = [x.split()[2].split("=") for x in folds]


def p1(points, i):
    axis, line = folds[i]
    line = int(line)
    res = set()
    if axis == "y":
        for x, y in points:
            if y > line:
                y = line - (y - line)
            res.add((x, y))
    else:
        for x, y in points:
            if x > line:
                x = line - (x - line)
            res.add((x, y))

    return res


def p2(points):
    for i in range(len(folds)):
        points = p1(points, i)
    x = max(points)[0]
    y = max(points, key=lambda p: p[1])[1]
    grid = [[" " for _ in range(x + 1)] for _ in range(y + 1)]
    for a, b in points:
        grid[b][a] = "█"

    return grid


print(len(p1(points, 0)))
for thing in p2(points):
    print("".join(thing))
