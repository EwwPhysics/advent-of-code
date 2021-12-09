from collections import Counter


with open("input.txt") as fin:
    data = [[x.split(), y.split()] for x, y in [x.split(" | ") for x in fin.read().splitlines()]]


def p1():
    c = 0
    for _, x in data:
        c += sum(len(y) in (2, 4, 3, 7) for y in x)
    return c


def p2():
    res = 0

    for x, y in data:
        c = Counter("".join(x))
        d = {
            0: "abcefg",
            1: "cf",
            2: "acdeg",
            3: "acdfg",
            4: "bcdf",
            5: "abdfg",
            6: "abdefg",
            7: "acf",
            8: "abcdefg",
            9: "abcdfg",
        }

        m = {}
        ca = set()
        dg = set()
        for k, v in c.items():
            if v == 9:
                m[k] = "f"
            elif v == 8:
                ca.add(k)
                m[k] = "ca"
            elif v == 7:
                dg.add(k)
                m[k] = "dg"
            elif v == 6:
                m[k] = "b"
            elif v == 4:
                m[k] = "e"
            else:
                print("help")

        for pat in x:
            if len(pat) == 2:
                val = (set(pat) & ca).pop()
                m[val] = "c"
                m[(ca - {val}).pop()] = "a"
            elif len(pat) == 4:
                val = (set(pat) & dg).pop()
                m[val] = "d"
                m[(dg - {val}).pop()] = "g"


        d_rev = {v: str(k) for k, v in d.items()}
        num = ""
        for pat in y:
            num += d_rev["".join(sorted(m[x] for x in pat))]
        res += int(num)

    return res


print(p1())
