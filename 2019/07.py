from intcode import Computer
from itertools import permutations


def p1():
    c = Computer("input.txt")
    m = 0
    for phases in permutations(range(5)):
        prev = 0
        for i in range(5):
            prev = c.run([phases[i], prev])[-1]
        if prev > m:
            m = prev
        c.reset()
    return m


def p2():
    pass


print(p1())
