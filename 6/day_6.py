from functools import reduce
from types import FunctionType
import operator

from inp import INPUT

def parse_op(op) -> FunctionType:
    match op:
        case "+": return operator.add
        case "*": return operator.mul
        case _ : return None # type: ignore

def part_one():
    input_split = list(map(str.split, INPUT.split("\n")))
    num_args = len(input_split) - 1
    num_problems = len(input_split[0])

    total = 0
    for problem in range(num_problems):
        args = map(int, [line[problem] for line in input_split[:num_args]])
        op = parse_op(input_split[num_args][problem])
        total += reduce(op, args)

    return total

def part_two():
    lines = INPUT.split('\n')
    width = max(map(len, lines))
    height = len(lines)

    # start at top right, work down and then left
    # when see an operator process the columns
    # (since the operators are all left-aligned)
    total = 0
    args = []
    for x in range(width, -1, -1):
        op = None
        num = ""
        # read the number vertically, add it to args
        for y in range(height):
            char = lines[y][x:x+1]
            if (op := parse_op(char)) == None:
                num += char
        if num.strip():
            args.append(int(num))

        # if the last thing was an operator consume all the args
        if op != None:
            total += reduce(op, args)
            args.clear()

    return total

print(part_one())
print(part_two())