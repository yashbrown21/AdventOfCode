import re
import sys

with open(r"Day1\input_d1.txt") as f:
    commands = [command.rstrip() for command in f]

start = 50
count = 0
special_case = False

for command in commands:
    if start == 0:
        special_case = True

    turn = int(command[1:])
    count += int(abs(turn/100))
    move = turn % 100

    if command[0] == "L":
        start -= move

    elif command[0] == "R":
        start += move

    # Start filtering
    if start % 100 == 0:
        count += 1
        start = 0

    elif start < 0:
        count += 0 if special_case else 1
        start += 100

    elif start > 99:
        count += 1
        start = start % 100

    # print(command, start, count)
    # print("-----")

    if special_case:
        special_case = False

print(count)

# 6431 too high
# 6016 wrong
# 5752 too low