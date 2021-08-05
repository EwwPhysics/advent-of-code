with open("input.txt") as file:
    fuels = map(int, file.read().splitlines())

def p1():
    return sum(n // 3 - 2 for n in fuels)


def p2():
    s = 0
    for n in fuels:
        while n > 0:
            n //= 3
            n -= 2
            s += n
    return s


print(p2())
