from intcode import Computer
from itertools import permutations, cycle


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
    amps = [Computer("input.txt") for _ in range(5)]
    m = 0
    for phases in permutations(range(5, 10)):
        prev = 0
        c = 0
        for phase, a in zip(phases, amps):
            a.inp.append(phase)
        for i, a in cycle(enumerate(amps)):
            if i == 0:
                c += 1
            out = a.run([prev])
            if len(out) < c:
                break
            prev = out[-1]
        if prev > m:
            m = prev
        for a in amps:
            a.reset()
    return m


print(p2())
