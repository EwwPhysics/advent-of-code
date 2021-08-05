with open('inputs/input15.txt') as fin:
    a = [int(x) for x in (fin.read()).split(',')]


def solve(data, number):
    loc = {index: value for value, index in enumerate(data[:-1])}
    num = data[-1]
    index = len(data) - 2
    while index < (number - 2):
        if num in loc:
            store = loc[num]
            loc[num] = index + 1
            num = index - store + 1
            index += 1
        else:
            loc[num] = index + 1
            num = 0
            index += 1
    return num


print(solve(a, 2020))
print(solve(a, 30000000))
