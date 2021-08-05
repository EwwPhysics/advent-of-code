with open('inputs/input18.txt') as fin:
    a = [x for x in (fin.read()).split('\n')]


def part_1(data):
    result = []
    for a, b in enumerate(data):
        while '(' in b:
            l_paren = b.rfind('(')
            r_paren = b.find(')', l_paren)
            within = b[l_paren + 1:r_paren]
            b = b[:l_paren] + str(evaluate(within)) + b[r_paren + 1:]
        result.append(evaluate(b))
    return sum(result)


def evaluate(expression):
    result = ''
    count = 0
    for i, x in enumerate(expression[:-1]):
        if x.isdigit() and expression[i + 1] == ' ' and i >= 3:
            result += x + ')'
            count += 1
        else:
            result += x
    return eval(('(' * (count + 1)) + result + expression[-1] + ')')


def part_2(data):
    return sum([eval('(' + b.replace('*', ') * (') + ')') for b in data])


print(part_1(a))
print(part_2(a))
