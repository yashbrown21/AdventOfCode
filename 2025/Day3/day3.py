import re
import sys
import numpy as np

with open(r"Day3\input_d3.txt") as f:
    data = f.readlines()

    banks = [ [int(num) for num in list(line.rstrip())] for line in data]

joltage = 0
part2 = True

for bank in banks:

    if part2:
        current_joltage = 0
        add_num_index = 0
        bank_jolt = 0

        for i in range(-11, 1, 1):
            if i == 0:
                search_bank = bank[add_num_index:]

            else:
                search_bank = bank[add_num_index:i]

            add_num = max(search_bank)
            add_num_index = add_num_index + search_bank.index(add_num) + 1
            bank_jolt += add_num * ( 10 ** -i ) 
            
        joltage += bank_jolt
        
    else:   
        first_num = max(bank)
        first_index = bank.index(first_num)

        if first_index == len(bank) - 1:
            second_num = first_num
            first_num = max(bank[:-1])

        else:
            second_num = max(bank[first_index+1:])

        joltage += first_num*10 + second_num

print(joltage)