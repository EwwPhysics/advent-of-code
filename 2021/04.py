with open("input.txt") as f:
    f = f.read().split("\n\n")
    drawn = [int(x) for x in f[0].split(",")]
    boards = [[[int(z) for z in y.split()] for y in x.splitlines()] for x in f[1:]]


def loops(func):
    def wrapper():
        b = set(range(len(boards)))
        for n in drawn:
            done = set()
            for board_index in b:
                board = boards[board_index]
                for i in range(len(board)):
                    if n in board[i]:
                        j = board[i].index(n)
                        board[i][j] = -1
                        if check_win(board, i, j):
                            if (
                                res := func(
                                    board=board,
                                    n=n,
                                    b=b,
                                    board_index=board_index,
                                    done=done,
                                )
                            ) != None:
                                return res
            b -= done

    return wrapper


@loops
def p1(**kwargs):
    return calc_score(kwargs["board"], kwargs["n"])


@loops
def p2(**kwargs):
    if len(kwargs["b"]) == 1:
        return calc_score(kwargs["board"], kwargs["n"])
    kwargs["done"].add(kwargs["board_index"])


def calc_score(board, n):
    return sum(sum(y for y in x if y != -1) for x in board) * n


def check_win(board, i, j):
    return all(x == -1 for x in board[i]) or all(
        board[k][j] == -1 for k in range(len(board))
    )
