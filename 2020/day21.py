from collections import Counter

with open('inputs/input21.txt') as fin:
    raw = fin.read()


def parse(data):
    data = data.replace(',', '')
    x = [x for x in (data.replace(')', '')).split('\n')]
    y = [[i[:i.index('(')].split(), i[i.index('('):].split()[1:]] for i in x]
    allergens = set([item for sublist in [i[1] for i in y] for item in sublist])
    dictionary = {i: [] for i in allergens}
    flat = [item for sublist in [i[0] for i in y] for item in sublist]
    for i in y:
        for n in i[1]:
            if not dictionary[n]:
                dictionary[n] = i[0]
            else:
                add = [num for num in i[0] if num in dictionary[n]]
                value = dictionary[n] + add
                dictionary[n] = value
    return dictionary, flat


def part_1(data, flat_data):
    result = {}
    while len(result) < len(data):
        for key, value in data.items():
            most = Counter(value).most_common(1)[0][1]
            vals = set(ing for ing in value if value.count(ing) == most and ing not in result.values())
            if len(vals) == 1:
                result[key] = list(vals)[0]
    return len([x for x in flat_data if x not in result.values()]), result


def part_2(data):
    return ','.join([value for (key, value) in sorted(data.items())])


a = parse(raw)[0]
b = parse(raw)[1]

print(part_1(a, b)[1])
print(part_2(part_1(a, b)[1]))
