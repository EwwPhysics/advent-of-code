with open('inputs/input24.txt') as fin:
    raw = fin.read()


def parse(raw):
    x = [x for x in raw.splitlines()]
    return x


a = parse(raw)


def part_1(data):
    dictionary = {}
    for a in data:
        e = a.count('ne') + a.count('se')
        w = a.count('nw') + a.count('sw')
        x = e + 2 * (a.count('e') - e) - (w + 2 * (a.count('w') - w))
        y = a.count('n') - a.count('s')
        if (x, y) in dictionary:
            dictionary[(x, y)] = not dictionary[(x, y)]
        else:
            dictionary[(x, y)] = True
    return dictionary, sum(dictionary.values())


def part_2(data):
    result = {}
    print(data.items())
    for x in range(10):
        for i in data.items():
            count = 0
            x = i[0]
            y = i[1]
            if data.get((x + 2, y)):
                if data.get((x + 2, y)) == 1:
                    count += 1
            else:
                result[(x + 2, y)] = -1

            if data.get((x - 2, y)):
                if data.get((x - 2, y)) == 1:
                    count += 1
            else:
                result[(x - 2, y)] = -1

            if data.get((x + 1, y + 1)):
                if data.get((x + 1, y + 1)) == 1:
                    count += 1
            else:
                result[(x + 1, y + 1)] = -1

            if data.get((x - 1, y + 1)):
                if data.get((x - 1, y + 1)) == 1:
                    count += 1
            else:
                result[(x - 1, y + 1)] = -1

            if data.get((x + 1, y - 1)):
                if data.get((x + 1, y - 1)) == 1:
                    count += 1
            else:
                result[(x + 1, y - 1)] = -1

            if data.get((x - 1, y - 1)):
                if data.get((x - 1, y - 1)) == 1:
                    count += 1
            else:
                result[(x - 1, y - 1)] = -1

            if data[i] == 1 and (count == 0 or count > 2):
                result[i] = -1
            elif data[i] == -1 and count == 2:
                result[i] = 1
            else:
                result[i] = data[i]
        data = result

    return list(result.values())


# print(a)
print(part_1(a)[1])
print(part_2(part_1(a)[0]))


