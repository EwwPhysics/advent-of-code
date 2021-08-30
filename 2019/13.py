from intcode import Computer
from collections import defaultdict


tiles = defaultdict(int)

def p1():
    return find_stuff()[0]


def find_stuff():
    c = Computer()
    while not c.finished:
        try:
            x, y, tile_id = c.run(m=3)
        except:
            break
        c.out = []

        tiles[x, y] = tile_id
        if tile_id == 4:
            ball = x
        elif tile_id == 3:
            paddle = x
    return len([x for x in tiles.values() if x == 2]), ball, paddle


def p2():
    c = Computer()
    _, ball, paddle = find_stuff()
    c.file[0] = 2
    score = 0

    while not c.finished:
        d = direction(ball, paddle)
        try:
            x, y, val = c.run(d, m=3, queue=False)
        except:
            break
        c.out = []

        if x == -1 and y == 0:
            score = val
        else:
            if val == 3:
                paddle = x
            elif val == 4:
                ball = x
            tiles[x, y] = val
    return score


def direction(ball, paddle):
    if ball < paddle:
        return -1
    elif ball > paddle:
        return 1
    return 0


print(p2())
