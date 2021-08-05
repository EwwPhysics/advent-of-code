with open('inputs/input10.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [int(x) for x in data.split('\n')] + [0]
    x.append(max(x) + 3)
    return x


a = parse(raw)
a.sort()

def part_1(x):
    data = x
    ratings = set(data)
    i = 0
    plus_one = set()
    plus_three = set()
    while i < len(data):
        if data[i] + 1 in ratings:
            plus_one.add(data[i])
        elif data[i] + 3 in ratings:
            plus_three.add(data[i])
        i += 1
    return [(len(plus_one) * len(plus_three)), plus_one, plus_three]


def is_valid(x, a):
    s = set(a)
    for i in x:
        if (i + 1 not in s) and (i + 2 not in s) and (i + 3 not in s):
            return False
    return True


def part_2(x):
    count = 0
    L = [num for num in x]
    for a, b in enumerate(x[1:-2]):
        L.remove(b)
        print(L)
        if is_valid(L, x):
            print(L)
            count += 1
        else:
            L.insert(a, b)
    return count


print(a)
print(part_2(a))
