with open('inputs/input2.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [x for x in data.split('\n')]
    return x


a = parse(raw)


def part_1(grid, h, v):
    num = 0
    count = 0
    for i in range(0, len(grid), v):
        num = num % len(grid[0])
        if grid[i][num] == '#':
            count += 1
        num += h
    return count


print(part_1(a, 3, 1))


def part_2(grid):
    result = 1
    l = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for i, x in l:
        result *= part_1(grid, i, x)
    return result


print(part_2(a))
