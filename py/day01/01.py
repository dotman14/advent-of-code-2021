with open("puzzle_input.txt", "r") as file_in:
    lines = [int(lines.rstrip()) for lines in file_in]

inc = 0
for i, e in enumerate(lines):
    if i == 0:
        if lines[i + 1] > lines[i]:
            inc += 1
    elif 0 < i < len(lines) - 1:
        if lines[i + 1] > lines[i]:
            inc += 1

print(inc)
