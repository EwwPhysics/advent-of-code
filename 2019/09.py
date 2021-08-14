from intcode import Computer


def p1():
    c = Computer("input.txt")
    return c.run([1])


def p2():
    c = Computer("input.txt")
    return c.run([2])


print(p2())
