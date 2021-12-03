from collections import Counter


with open("input.txt") as fin:
    data = fin.read().splitlines()
    zipped = list(zip(*data))


def p1():
    gamma = ""
    for x in zipped:
        c = Counter(x)
        gamma += c.most_common(1)[0][0]

    gamma = int(gamma, 2)
    elipson = gamma ^ (2 ** len(zipped) - 1)
    return gamma * elipson


def p2():
    x = data[find_rating(True)]
    y = data[find_rating(False)]
    return int(x, 2) * int(y, 2)


def find_rating(o: bool):
    indices = set(range(len(data)))
    for x in zipped:
        c = Counter(x[i] for i in indices)
        comp = c["1"] >= c["0"] if o else c["0"] > c["1"]
        thing = "1" if comp else "0"
        for i in range(len(x)):
            if x[i] != thing:
                indices.discard(i)

        if len(indices) == 1:
            return indices.pop()

    raise Exception("hmm")


print(p1())
