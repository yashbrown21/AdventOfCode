import re
import numpy as np
from itertools import combinations
from collections import Counter
import sympy
from scipy.optimize import linprog
import sys
import itertools

part1 = False
test = False
filename = r"Day10\test_d10.txt" if test else r"Day10\input_d10.txt"

machines = {}

# --------------------------------------------------------
## Data Parsing
# --------------------------------------------------------
def parse_string_tuples(s):
    # Find paranthesis groups
    groups = re.findall(r'\((.*?)\)', s)

    result = []

    for group in groups:
        # Split by comma, strip whitespace, convert to int
        nums = [int(x) for x in group.split(',') if x.strip() != ""]

        # Convert to tuple
        result.append(tuple(nums))

    return result

# --------------------------------------------------------
## Part 1
# --------------------------------------------------------
def check_tuple_list(target, button_combi):
    button_moves = [i for sub in button_combi for i in sub]
    button_counts = Counter(button_moves)
    actual_lights_on = tuple(sorted(set([i for i in button_moves if button_counts[i] % 2 != 0])))

    if actual_lights_on == target:
        return True
    else:
        return False
    
def min_config_buttons(target, buttons):
    for i in range(1, len(buttons) + 1):
        combis = combinations(buttons, i)

        if any([check_tuple_list(target, combi) for combi in combis]):
            return i
        else:
            continue

    return i

# --------------------------------------------------------
## Part 2
# --------------------------------------------------------
def min_joltage_buttons(target, buttons):
    button_matrix = np.array([[1 if i in button else 0 for i in range(len(target))] for button in buttons], dtype = int).T
    b = np.array(target, dtype=int)
    c = np.ones(len(buttons), dtype=int)

    res = linprog(
        c,
        A_eq=button_matrix,
        b_eq=b,
        bounds=[(0, None)]*len(buttons),  # x_j >= 0
        integrality=1                     # enforce integers
    )

    return int(np.sum(res.x))

### I GIVE UP ON SYMPY
def min_joltage_buttons_broken(target, buttons):
    button_matrix = [[1 if i in button else 0 for i in range(len(target))] for button in buttons] + [target]
    joltage_matrix = sympy.Matrix(button_matrix).T

    jm_rref, jm_pivots = joltage_matrix.rref()
    jm_pivots = list(jm_pivots)
    jm_non_pivots = [i for i in range(joltage_matrix.shape[1]-1) if i not in jm_pivots]
    row_pivots = list(range(len(jm_pivots)))
    
    A = jm_rref.extract(row_pivots, list(range(joltage_matrix.shape[1]-1)))
    b = jm_rref.extract(row_pivots, [joltage_matrix.shape[1]-1])

    A_ind, A_dep = A.extract(range(A.rows), jm_pivots), A.extract(range(A.rows), jm_non_pivots)

    free_vars = len(jm_non_pivots)

    if free_vars > 0:
        d = A_ind.LUsolve(b)
        C = A_ind.LUsolve(A_dep)
        
        upper_bounds = []

        for j in range(free_vars):
            bounds_j = []
            for i in range(C.rows):
                if C[i,j] > 0:
                    bounds_j.append(d[i] / C[i,j])
            ub = int(sympy.floor(min(bounds_j))) if bounds_j else int(max(target))
            upper_bounds.append(ub)

        axes = [range(ub + 1) for ub in upper_bounds]
        jolt_min = sympy.oo

        for x2_tuple in itertools.product(*axes):
            x2 = sympy.Matrix(x2_tuple)
            x = A_ind.LUsolve(b - A_dep * x2)
            
            # Only consider non-negative integers
            if all(x_i.is_integer and x_i >= 0 for x_i in x) and all(x2_i >= 0 for x2_i in x2):
                press_val = int(sum(x)) + int(sum(x2))
                if press_val < jolt_min:
                    jolt_min = press_val

        """ axes = [list(range(ub + 1)) for _ in range(free_vars)]
        grid = np.meshgrid(*axes, indexing='ij')

        X2_samples = np.stack([g.flatten() for g in grid], axis=-1)
        x0 = A_ind_inv @ b
        jolt_min = np.sum(x0) if np.all(x0 > 0) else np.inf

        for x2 in X2_samples:
            x = A_ind_inv @ (b - A_dep @ x2)
            press_val = np.sum(x) + np.sum(x2)

            if all(x >= 0) and press_val < jolt_min:
                jolt_min = press_val
        """

        if jolt_min == sympy.oo:
            print("Error")
        

        return int(jolt_min)
    
    else:
        return sum(A_ind.LUsolve(b))

with open(filename) as f:
    for i, line in enumerate(f.readlines()):
        line_data = line.split()
        target = tuple([i for i, char in enumerate(line_data[0][1:-1]) if char == "#"])
        joltage = [int(i) for i in line_data[-1][1:-1].split(",")]
        buttons = parse_string_tuples("".join(line_data[1:-1]))

        machines[i] = {"light": target, "joltage": joltage, "buttons": buttons}

min_moves = []
min_voltages = []
for key, data in machines.items():
    min_moves.append(min_config_buttons(data["light"], data["buttons"]))
    min_voltages.append(min_joltage_buttons(data["joltage"], data["buttons"]))
    
print(f"Part 1: {sum(min_moves)}")
print(f"Part 2: {sum(min_voltages)}")