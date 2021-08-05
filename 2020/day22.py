from collections import deque

with open('inputs/input22.txt') as fin:
    raw = fin.read()


def parse(data):
    data = data.split('\n\n')
    x = deque([int(x) for x in data[0].split('\n')[1:]])
    y = deque([int(y) for y in data[1].split('\n')[1:]])
    return x, y


a = parse(raw)[0]
b = parse(raw)[1]

def nums():
    n = 1
    while True:
        yield n
        n += 1


def part_1(a, b):
    while a and b:
        if a[0] > b[0]:
            a.append(a.popleft())
            a.append(b.popleft())
        else:
            b.append(b.popleft())
            b.append(a.popleft())
    result = 0
    gen = nums()
    if a:
        res = a
    else:
        res = b
    for i in reversed(res):
        result += i * next(gen)
    return result


# def part_2(a, b):





print(a)
print(b)
print(part_1(a, b))
# print(part_2(a))
