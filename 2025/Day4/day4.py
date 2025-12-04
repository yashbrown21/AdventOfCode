import re
import numpy as np

part1 = False

with open(r"Day4\input_d4.txt") as f:
    data = f.readlines()

    maze = np.array([list(line.rstrip()) for line in data])

dir_8 = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
rows, cols = maze.shape
rolls_dict = {}

for x in range(rows):
    for y in range(cols):
        if maze[x,y] == "@":
            pos = x + 1j*y

            surround_rolls = 0

            for dir in dir_8:
                z = pos + dir
                nx, ny = int(z.imag), int(z.real)

                # Bounds check
                if 0 <= nx < rows and 0 <= ny < cols:
                    if maze[ny, nx] == "@":
                        surround_rolls += 1

            rolls_dict[pos] = surround_rolls

if part1:
    print(sum(value < 4 for value in rolls_dict.values()))

else:
    total_rolls = 0
    new_rolls = 0

    while total_rolls == 0 or new_rolls != 0:

        new_rolls = 0
        removable_rolls = [key for key,val in rolls_dict.items() if val < 4]

        for key in removable_rolls:
            for dir in dir_8:
                z = key + dir

                if z in rolls_dict.keys():
                    rolls_dict[z] -= 1

        for k in removable_rolls:
            new_rolls += 1
            rolls_dict.pop(k, None)

        total_rolls += new_rolls

    print(total_rolls)

""" def removable_rolls(grid):
    rolls = 0
    rows, cols = grid.shape

    for x in range(rows):

        for y in range(cols):
            pos = x + 1j*y

            if maze[x,y] == ".":
                continue

            count = 0

            for dir in dir_8:
                z = pos + dir
                nx, ny = int(z.imag), int(z.real)

                # Bounds check
                if 0 <= nx < rows and 0 <= ny < cols:
                    if maze[ny, nx] == "@":
                        count += 1


                if count >= 4:
                    break

            if count < 4:
                rolls += 1

    

print(total_rolls) """