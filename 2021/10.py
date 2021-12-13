from statistics import median


corrupt_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

incomplete_scores = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

opposites = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

with open("input.txt") as fin:
    data = fin.read().splitlines()


def p1():
    res = 0
    for line in data:
        d = []
        for char in line:
            if char in incomplete_scores:
                d.append(char)
            else:
                if char != opposites[d.pop()]:
                    res += corrupt_scores[char]
                    break
    return res


def check_valid(line):
    d = []
    for char in line:
        if char in ("(", "[", "{", "<"):
            d.append(char)
        else:
            if char != opposites[d.pop()]:
                return False
    return True


def p2():
    res = []
    for line in data:
        if check_valid(line):
            d = []
            for char in line:
                if char in ("(", "[", "{", "<"):
                    d.append(char)
                else:
                    d.pop()
            score = 0
            for x in reversed(d):
                score *= 5
                score += incomplete_scores[x]
            res.append(score)
    return median(res)
  
