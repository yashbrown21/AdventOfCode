import re
import sys
import os 
from functools import cache

part1 = False
test = False
filename = r"Day7\test_d7.txt" if test else r"Day7\input_d7.txt"
DATA = []

with open(filename) as f:
    DATA = [list(line) for line in f.readlines()]

if part1:
    splits = 0

    for i in range(1, len(DATA)):
        for j in range(len(DATA[i])):
            if DATA[i-1][j] == "S" or DATA[i-1][j] == "|":
                if DATA[i][j] == "^":
                    if j >= 0:
                        DATA[i][j-1] = "|"
                    if j < len(DATA[i]):
                        DATA[i][j+1] = "|"

                    splits += 1
                
                else:
                    DATA[i][j] = "|"

    print(splits)

else:
    @cache
    def find_path(x, y):
        if x >= len(DATA) and (0 <= y < len(DATA[0])):
            return 1
        
        elif (0 > y or y > len(DATA[0])):
            return 0
        
        elif DATA[x][y] == "^":
            return find_path(x+1, y-1) + find_path(x+1, y+1)
        
        else:
            return find_path(x+1, y)
    
    loc_S = DATA[0].index("S")

    paths = find_path(1, loc_S)
    print(paths)