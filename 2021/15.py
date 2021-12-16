import copy
import queue

with open("input.txt") as fin:
    board = [[int(x) for x in line] for line in fin.read().splitlines()]


def solve(cavern):
    N = len(cavern)
    M = len(cavern[0])

    q = queue.PriorityQueue()
    q.put((0, (0, 0)))

    v = set()

    while True:
        val, (i, j) = q.get()
        if (i, j) == (N - 1, M - 1):
            return val
        for y, x in get_neighbors(i, j):
            if y in range(N) and x in range(M) and (y, x) not in v:
                v.add((y, x))
                q.put((val + cavern[y][x], (y, x)))


def large_board():
    new_board = copy.deepcopy(board)
    for i, row in enumerate(board):
        for j in range(4):
            new_board[i].extend([(x + j) % 9 + 1 for x in row])

    for i in range(4):
        for j in range(len(board)):
            row = [x % 9 + 1 for x in new_board[j + (len(board) * i)]]
            new_board.append(row)

    return new_board


def get_neighbors(i, j):
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


print(solve(board))
print(solve(large_board()))
