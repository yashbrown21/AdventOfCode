import re
import sys
import numpy as np

part1 = True
test = False

filename = r"Day12\test_d12.txt" if test else r"Day12\input_d12.txt"

shapes = {}
areas = {}
trees = []

with open(filename) as f:
    data = f.readlines()
    split_val = 30
    i = 0

    while i < len(data):
        line = data[i].strip()
        key, val = line.split(":")

        if not val:  
            shape = data[i+1:i+4] 
            shapes[int(key)] = [[ 1 if char == "#" else 0 for char in list(l.rstrip()) ] for l in shape]
            areas[int(key)] = np.array(shapes[int(key)]).sum()
            i += 5

        else:
            val = val[1:]
            key = tuple( [ int(s) for s in key.split('x') ] )
            trees.append([key , dict(enumerate([int(k) for k in val.split()]))])
            i += 1

if part1:
    regions = 0

    for tree in trees:
        tree_area, presents = tree
        avi_area = np.prod(tree_area)
        present_area = sum(areas[key]*val for key,val in presents.items())

        if avi_area < present_area:
            continue

        elif avi_area >= sum(9*val for val in presents.values()):
            regions += 1

        else:
            # General solver for permutations of shapes
            continue
            
    print(regions)