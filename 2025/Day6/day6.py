import re
import numpy as np
import operator
import os

part1 = False
test = False

ops = { "+": lambda x: np.sum(x, dtype = np.float64), "*": lambda x: np.prod(x, dtype = np.float64) }
filename = r"Day6\test_d6.txt" if test else r"Day6\input_d6.txt" 

if part1:
    with open(filename) as f:
        problems = np.loadtxt(f, dtype=str)

    count = 0

    for problem in problems.T:
        oper = problem[-1]
        vals = np.array([int(num) for num in problem[:-1]], dtype = np.float64)

        count += ops[oper](vals)

    print(count)

else:
    with open(filename) as f:
        data = f.readlines()

    matrix = [list(line.rstrip('\r').rstrip('\n')) for line in data[:-1]]
    operators = np.array(data[-1].split())

    problems = np.array(matrix)[:, ::-1]

    i = len(operators) - 1
    num_arr = []
    count = np.dtype('int64').type(0)

    for num in problems.T:
        if not ''.join(num).isspace():
            num_arr.append(int(''.join(num)))
        
        else:
            count += ops[operators[i]](num_arr)
            i -= 1
            num_arr = []
    
    count += ops[operators[0]](num_arr)
    print(count)