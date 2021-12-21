from itertools import cycle, islice, product
from functools import cache


s1, s2 = 10, 1


def play(p1, p2):
    count = cycle(range(1, 101))
    score1, score2 = 0, 0
    res = 0
    while True:
        p1 = (p1 + sum(islice(count, 3)) - 1) % 10 + 1
        p2 = (p2 + sum(islice(count, 3)) - 1) % 10 + 1
        score1 += p1
        if score1 >= 1000:
            return score2 * (res + 3)
        score2 += p2
        if score2 >= 1000:
            return score1 * (res + 6)
        res += 6


@cache
def part_2(p1, p2, score1, score2, turn):
    A, B = 0, 0
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1
    for x in product([1, 2, 3], repeat=3):
        if turn == 0:
            temp_p1 = (p1 + sum(x) - 1) % 10 + 1
            a, b = part_2(temp_p1, p2, score1 + temp_p1, score2, not turn)
        else:
            temp_p2 = (p2 + sum(x) - 1) % 10 + 1
            a, b = part_2(p1, temp_p2, score1, score2 + temp_p2, not turn)
        A += a
        B += b
    return A, B


print(play(s1, s2))
print(max(part_2(s1, s2, 0, 0, 0)))
