import re

with open("input.txt") as fin:
    m = re.match(r"target area: x=([-\d]*)\.\.([-\d]*), y=([-\d]*)\.\.([-\d]*)", fin.read())
    x1, x2, y1, y2 = map(int, m.groups())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)


def p1():
    return y1 * (y1 + 1) // 2


def p2():
    res = 0
    for x in range(-100, x2 + 1):
        for y in range(y1, abs(y1)):
            res += is_valid(x, y)
    return res


def is_valid(x, y):
    x_pos, y_pos = 0, 0
    while not (
        y_pos < y1 and y <= 0
        or x_pos > x2
        or x <= 0 and x_pos < x1
    ):
        if x1 <= x_pos <= x2 and y1 <= y_pos <= y2:
            return True
        x_pos += x
        y_pos += y
        x = x - 1 if x > 0 else x + 1 if x < 0 else 0
        y -= 1
    return False
