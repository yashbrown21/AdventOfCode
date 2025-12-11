import re
import numpy as np
from itertools import combinations
import shapely

part1 = False
test = False
filename = r"Day9\test_d9.txt" if test else r"Day9\input_d9.txt"

with open(filename) as f:
    points = [tuple(map(int, line.split(','))) for line in f.readlines()]

if part1:
    max_area = max((abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1) for p1, p2 in combinations(points, 2))

    print(f"Part 1: {max_area}")

else:
    polygon = shapely.geometry.Polygon(points)
    max_area = 0

    for p1, p2 in combinations(points,2):
        x1, y1 = p1
        x2, y2 = p2

        vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)] 
        rect_poly = shapely.geometry.Polygon(vertices)

        if polygon.covers(rect_poly):
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = area if area > max_area else max_area

    print(f"Part 2: {max_area}")