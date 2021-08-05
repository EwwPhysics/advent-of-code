with open('inputs/input2.txt') as fin:
    raw = fin.read()


def parse(raw):
    start = [(x[:3], int(x[4:])) for x in (raw.split('\n'))]
    return start


a = parse(raw)


def part_1(arr):
    indices = set()
    acc = 0
    i = 0
    while i < len(arr):
        pair = arr[i]
        if i in indices:
            break
        indices.add(i)
        if pair[0] == 'acc':
            acc += pair[1]
            i += 1
        elif pair[0] == 'jmp':
            i += pair[1]
        else:
            i += 1
    return acc


def not_infinite(arr):
    indices = set()
    acc = 0
    i = 0
    while True:
        if i in indices:
            return 0
        indices.add(i)
        if i == len(arr):
            return acc
        pair = arr[i]
        if pair[0] == 'acc':
            acc += pair[1]
            i += 1
        elif pair[0] == 'jmp':
            i += pair[1]
        else:
            i += 1


def part_2(arr):
    for i, x in enumerate(arr):
        if x[0] == 'jmp':
            test = arr[:i] + [('nop', x[1])] + arr[i + 1:]
            if c := not_infinite(test):
                return c
        if x[0] == 'nop':
            test = arr[:i] + [('jmp', x[1])] + arr[(i + 1):]
            if c := not_infinite(test):
                return c


print(part_1(a))
print(part_2(a))
