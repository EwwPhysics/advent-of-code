with open('inputs/input5.txt') as fin:
    raw = fin.read()


def parse(data):
    trans = str.maketrans('RLBF', '1010')
    x = [x.translate(trans) for x in data.split('\n')]
    return x


a = parse(raw)


def part_1(passes):
    seat = [(int(x[:7], 2) * 8) + int(x[-3:], 2) for x in passes]
    seat.sort()
    return seat


seats = part_1(a)
print(seats[-1])


def part_2(seats):
    count = sum(range(seats[0], (seats[-1] + 1)))
    return count - sum(seats)


print(part_2(seats))
