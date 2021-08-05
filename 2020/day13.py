import math


with open('inputs/input13.txt') as fin:
    raw = fin.read()

i = [x for x in raw.split('\n')]
time = i[0]
a = [int(x) for x in i[1].split(',') if x.isdecimal()]


def part_1(data):
    soon = 1000303 + data[0]
    id = data[0]
    for x in data:
        num = -(1000303 % x) + x
        if num < soon:
            soon = num
            id = x
    return id * soon


def part_2(data):
    x = math.lcm(*data)


print(a)
print(part_2(a))
