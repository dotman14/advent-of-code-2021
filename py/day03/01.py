from collections import Counter

with open("input.txt", "r") as file_input:
    idx_dict = {}
    for val1 in file_input:
        for idx, val2 in enumerate(val1.rstrip()):
            if idx in idx_dict:
                idx_dict[idx].append(val2)
            else:
                idx_dict[idx] = [val2]


def binary_and_flip(bin_dict):
    bin_str = ""
    for i in bin_dict:
        bin_str += Counter(bin_dict[i]).most_common(1)[0][0]
    flipped_bin = "".join("0" if x == "1" else "1" for x in bin_str)
    return int(bin_str, 2) * int(flipped_bin, 2)


print(binary_and_flip(idx_dict))
