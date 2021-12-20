import collections

with open("input.txt", "r") as file_in:
    lines = [lines for lines in file_in.readlines() if lines != "\n"]
    start = lines.pop(0).rstrip()
    key_value = {}
    for i in lines:
        k_v = i.rstrip().split(" -> ")
        key_value[k_v[0]] = k_v[1]


def insert_values(start_polymer):
    end_polymer = []
    for i, j in enumerate(start_polymer):
        lookup = start_polymer[i: i + 2]
        end_polymer.append(j)
        end_polymer.append(key_value.get(lookup, ""))
    return ''.join(end_polymer)


def recurse(stt, n):
    if n == 0:
        return stt
    output = insert_values(stt)
    print(n)
    return recurse(output, n - 1)


after_n_times = recurse(start, 40)
freq = collections.Counter(after_n_times).values()
print(max(freq) - min(freq))
