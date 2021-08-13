W = 25
H = 6

with open("input.txt") as fin:
    file = fin.read().strip()
    layers = []
    for i in range(0, len(file), W * H):
        layer = []
        for j in range(i, i + W * H, W):
            layer.append(file[j: j + W])
        layers.append(layer)


def p1():
    zeros = float("inf")
    l = 0
    for i, layer in enumerate(layers):
        layers[i] = [item for sublist in layer for item in sublist]
        if (z := layers[i].count("0")) < zeros:
            l = i
            zeros = z
    print(l)
    return layers[l].count("1") * layers[l].count("2")

def p2():
    res = []
    for r in zip(*layers):
        layer = []
        for p in zip(*r):
            layer.append([x for x in p if x != "2"][0])
        res.append(layer)
    return res

for l in p2():
    print("".join(l).replace("0", " ").replace("1", "█"))
