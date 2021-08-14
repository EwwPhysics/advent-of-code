from collections import deque, defaultdict


class Computer:
    def __init__(self, file="input.txt"):
        with open(file) as fin:
            self.file = defaultdict(int)
            for i, val in enumerate(map(int, fin.read().split(","))):
                self.file[i] = val
        self.FILE: defaultdict = self.file.copy()
        self.NUMS = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}
        self.out = []
        self.i = 0
        self.inp = deque()
        self.base = 0

    def run(self, inp):
        self.inp.extend(inp)
        while self.i < len(self.file):
            op, modes = Computer.parse_token(self.file[self.i])
            params = self.parameters(self.i, op, modes)
            increase = True
            if op == 1:
                self.file[params[2]] = self.file[params[0]] + self.file[params[1]]
            elif op == 2:
                self.file[params[2]] = self.file[params[0]] * self.file[params[1]]
            elif op == 3:
                self.file[params[0]] = self.inp.popleft()
            elif op == 4:
                self.out.append(self.file[params[0]])
            elif op == 5:
                if self.file[params[0]] != 0:
                    self.i = self.file[params[1]]
                    increase = False
            elif op == 6:
                if self.file[params[0]] == 0:
                    self.i = self.file[params[1]]
                    increase = False
            elif op == 7:
                if self.file[params[0]] < self.file[params[1]]:
                    self.file[params[2]] = 1
                else:
                    self.file[params[2]] = 0
            elif op == 8:
                if self.file[params[0]] == self.file[params[1]]:
                    self.file[params[2]] = 1
                else:
                    self.file[params[2]] = 0
            elif op == 9:
                self.base += self.file[params[0]]
            elif op == 99:
                break
            else:
                raise Exception("hm")
            if increase:
                self.i += self.NUMS[op]
        return self.out

    @staticmethod
    def parse_token(n):
        op = n % 100
        n //= 100
        modes = map(int, reversed(list(str(n).rjust(3, "0"))))
        return op, modes

    def parameters(self, i, op, modes):
        params = []
        if op == 99:
            return params
        n = self.NUMS[op]
        inp = [x for x in range(i + 1, i + n)]
        for p, mode in zip(inp, modes):
            if mode == 1:
                params.append(p)
            elif mode == 0:
                params.append(self.file[p])
            elif mode == 2:
                params.append(self.file[p] + self.base)
        return params

    def reset(self):
        self.file = self.FILE.copy()
        self.i = 0
        self.out = []
        self.inp = deque()
        self.base = 0

