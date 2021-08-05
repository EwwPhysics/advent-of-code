import intcode


def p1():
    c = intcode.Computer("input.txt")
    c.file[1] = 12
    c.file[2] = 2
    return c.run()

def p2():
    c = intcode.Computer("input.txt")
    for i in range(100):
        for j in range(100):
            c.file[1] = i
            c.file[2] = j
            if c.run() == 19690720:
                return 100 * i + j
            c.reset()

print(p2())
