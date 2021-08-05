with open('inputs/input2.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [x for x in data.split('\n\n')]
    for a, b in enumerate(x):
        b = b.replace('\n', ' ')
        x[a] = [i for i in b.split(' ')]
        for c, d in enumerate(x[a]):
            x[a][c] = d.split(':')
    return x


a = parse(raw)


def part_1(data):
    count = 0
    for passport in data:
        cid = 0
        for key, value in passport:
            if key == 'cid':
                cid += 1
        if len(passport) - cid >= 7:
            count += 1
    return count


print(part_1(a))


def check(pairs):
    valid = True
    cid = 0
    for a, b in pairs:
        if a == 'byr':
            if int(b) not in range(1920, 2003):
                valid = False
        elif a == 'iyr':
            if int(b) not in range(2010, 2021):
                valid = False
        elif a == 'eyr':
            if int(b) not in range(2020, 2031):
                valid = False
        elif a == 'hgt':
            if b.endswith('cm'):
                if int(b[:-2]) not in range(150, 194):
                    valid = False
            elif b.endswith('in'):
                if int(b[:-2]) not in range(59, 77):
                    valid = False
            else:
                valid = False
        elif a == 'hcl':
            hcl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            if b[0] != '#' or len(b) != 7:
                valid = False
            else:
                for char in b[1:]:
                    if char not in hcl:
                        valid = False
        elif a == 'ecl':
            ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if b not in ecl:
                valid = False
        elif a == 'pid':
            if b.isdigit():
                pass
            else:
                valid = False
            if len(b) != 9:
                valid = False
        else:
            cid += 1
    if len(pairs) - cid < 7:
        valid = False
    return valid


def part_2(data):
    count = 0
    for passport in data:
        if check(passport):
            count += 1
    return count

print(part_2(a))