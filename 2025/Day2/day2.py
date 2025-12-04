import numpy as np
import re
from collections import Counter

test = False
if test:
    file_name = r"Day2\test_d2.txt"
else:
    file_name = r"Day2\input_d2.txt"

with open(file_name) as f:
    data = f.read().rstrip()
    item_range = []

    for product_ranges in data.split(","):
        item_range.append([int(val) for val in product_ranges.split("-")])

count = 0

for prod_range in item_range:
    
    for i in range(prod_range[0], prod_range[1] + 1, 1):
        str_val = str(i)

        str_split_range = list(range(len(str_val)//2, 0, -1))

        for num in str_split_range:
            if len(str_val) % num != 0:
                continue;

            else:
                chunks = [str_val[i:i+num] for i in range(0, len(str_val), num)]
                rep_check = Counter(chunks)

                if len(list(rep_check.keys())) == 1:
                    count += i
                    break

        """ if len(str_val) % 2 != 0:
            continue;
        else:
            if str_val[:len(str_val)//2] == str_val[len(str_val)//2:]:
                count += i """

print(count)