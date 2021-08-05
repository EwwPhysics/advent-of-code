with open('inputs/input2.txt') as fin:
    puzzleinput = fin.read()


def parse(data):
    y = [x for x in data.split('\n')]
    for i, x in enumerate(y):
        y[i] = [x[:x.find('-')],
                x[(x.find('-') + 1): x.find(' ')],
                x[x.find(' ') + 1],
                x[(x.find(' ', (x.find(' ') + 1))) + 1:]]
    return y


a = parse(puzzleinput)


def part_1(L):
    count = 0
    for a, b, c, d in L:
        if d.count(c) in range(int(a), int(b) + 1):
            count += 1
    return count


def part_2(L):
    count = 0
    for a, b, c, d in L:
        num1 = int(a) - 1
        num2 = int(b) - 1
        if bool(d[num1] == c) ^ bool(d[num2] == c):
            count += 1
    return count
