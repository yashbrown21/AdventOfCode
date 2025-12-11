import re
import sys
import numpy
from itertools import combinations


part1 = False

fresh_range = []
ingredients = []

with open(r"Day5\input_d5.txt") as f:
    data = f.readlines()
    line_break = False

    for line in data:
        if not line.rstrip():
            line_break = True
            continue
        
        if not line_break:
            num1, num2 = line.rstrip().split("-")
            fresh_range += [(int(num1), int(num2))]

        else:
            ingredients += [int(line.rstrip())]

sorted(fresh_range)

if part1:
    count = 0;

    for ingredient in ingredients:
        for num1, num2 in fresh_range:
            if num1 <= ingredient <= num2:
                count += 1
                break

    print(count)

else:
    def check_overlapping_ranges(tuple_list):

        for range1, range2 in combinations(tuple_list, 2):
            min1, max1 = range1
            min2, max2 = range2

            if min1 > max2 or max1 < min2:
                continue
            else:
                return range1, range2
        pass
    
    while True:
        if not check_overlapping_ranges(fresh_range):
            break

        else:
            range1, range2 = check_overlapping_ranges(fresh_range)

            fresh_range.remove(range1)
            fresh_range.remove(range2)

            combi_range = range1 + range2
            fresh_range.append((min(combi_range), max(combi_range)))

    fresh_ingredients = 0 

    for num1, num2 in fresh_range:
        fresh_ingredients += num2 - num1 + 1

    print(fresh_ingredients)