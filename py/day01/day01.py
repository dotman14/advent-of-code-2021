with open('puzzle_input.txt', 'r') as file_in:
    l = [int(lines.rstrip()) for lines in file_in]
    inc = 0
    for i, e in enumerate(l):
        if i == 0:
            if l[i + 1] > l[i]:
                inc += 1
        elif 0 < i < len(l) - 1:
            if l[i + 1] > l[i]:
                inc += 1

print(inc)