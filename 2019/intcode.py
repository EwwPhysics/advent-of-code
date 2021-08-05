class Computer:
    def __init__(self, file):
        with open(file) as fin:
            self.file = list(map(int, fin.read().split(",")))
        self.FILE: list = self.file.copy()
        self.NUMS = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}

    def run(self, inp):
        i = 0
        out = []
        inp = iter(inp)
        while i < len(self.file):
            op, modes = Computer.parse_token(self.file[i])
            params = self.parameters(i, op, modes)
            increase = True
            if op == 1:
                self.file[params[2]] = self.file[params[0]] + self.file[params[1]]
            elif op == 2:
                self.file[params[2]] = self.file[params[0]] * self.file[params[1]]
            elif op == 3:
                self.file[params[0]] = next(inp)
            elif op == 4:
                out.append(self.file[params[0]])
            elif op == 5:
                if self.file[params[0]] != 0:
                    i = self.file[params[1]]
                    increase = False
            elif op == 6:
                if self.file[params[0]] == 0:
                    i = self.file[params[1]]
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
            elif op == 99:
                break
            else:
                raise Exception("hm")
            if increase:
                i += self.NUMS[op]
        return out

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
        return params
        
    def reset(self):
        self.file = self.FILE.copy()

