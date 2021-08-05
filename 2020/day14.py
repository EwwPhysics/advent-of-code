with open('inputs/input14.txt') as fin:
    raw = fin.read()


def parse(raw):
    a = [x for x in raw.split('\nmask')]
    for i, x in enumerate(a):
        test = x.split('\n')
        x = [test[0][test[0].find('=') + 2:], [[int(i[4:i.find(']')]), int(i[i.find('=') + 2:])] for i in test if i.startswith('mem')]]
        a[i] = x
    return a


a = parse(raw)


def part_1(data):
    mem = {}
    for x in data:
        mask = x[0]
        for a, b in x[1]:
            binary = str(bin(b))[2:]
            test = binary.rjust(36, '0')
            output = ''.join([x if mask[i] == 'X' else mask[i] for i, x in enumerate(test)])
            mem[a] = int(output, 2)
    return sum(mem.values())


def part_2(data):
    mem = {}
    for x in data:
        mask = x[0]
        for a, b in x[1]:
            binary = str(bin(a))[2:]
            test = binary.rjust(36, '0')
            addresses = ''.join(['1' if mask[i] == '1' else x if mask[i] == '0' else 'X' for i, x in enumerate(test)])
            for i in find_ad(addresses):
                mem[i] = b
    return sum(mem.values())


def find_ad(addresses):
    num = addresses.count('X')
    result = []
    floating = '0'*num
    while int(floating, 2) <= int('1'*num, 2):
        loc = addresses
        for x in floating:
            loc = loc.replace('X', x, 1)
        result.append(loc)
        floating = str(bin(int(floating, 2) + 1))[2:].rjust(num, '0')
    return result


print(part_2(a))
print(part_1(a))
