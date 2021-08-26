from intcode import Computer


def p1():
    return len(paint())


def p2():
    painted = paint(part=2)
    points = painted.keys()
    x = max(points, key=lambda x: x[0])[0] - (mx := min(points, key=lambda x: x[0])[0])
    y = max(points, key=lambda x: x[1])[1] - (my := min(points, key=lambda x: x[1])[1])
    arr = [["." for _ in range(x + 1)] for _ in range(y + 1)]
    for j, i in points:
        if painted[(j, i)]:
            arr[i - my][j - mx] = "#"
    return arr


def paint(part=1):
    c = Computer("input.txt")
    painted = {}
    x, y = (0, 0)
    d = 0

    if part == 2:
        painted[(0, 0)] = True

    while not c.finished:
        if (x, y) not in painted:
            painted[(x, y)] = False
        if len(output := c.run(int(painted[(x, y)]), m=2)) == 2:
            colour, direction = output
        c.out = []

        painted[(x, y)] = colour

        if direction == 1:
            d += 1
        else:
            d -= 1
        d %= 4
        diff = 1 if d in (0, 1) else -1
        if d in (0, 2):
            y += diff
        else:
            x += diff

    return painted


print(p1())

for line in reversed(p2()):
    print("".join(line))
