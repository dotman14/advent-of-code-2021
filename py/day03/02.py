from collections import Counter

with open("input.txt", "r") as file_input:
    lines = [line.rstrip() for line in file_input.readlines()]

    idx_dict = {}
for y in lines:
    for k, v in enumerate(y):
        if k in idx_dict:
            idx_dict[k].append(v)
        else:
            idx_dict[k] = [v]
print(idx_dict)