from intcode import Computer


def p1():
    c = Computer("input.txt")
    out = c.run(1)
    print(out)
    return out[-1]


def p2():
    c = Computer("input.txt")
    out = c.run(5)
    return out[-1]



