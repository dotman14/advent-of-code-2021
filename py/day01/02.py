with open("puzzle_input.txt", "r") as file_in:
    lines = [int(lines.rstrip()) for lines in file_in]


def sliding_window_sums(lst: list, window_size=3, stride=1) -> list:
    """Return a list of sums of sliding window"""
    w = []
    while lst:
        if len(lst[:window_size]) == window_size:
            w.append(sum(lst[:window_size]))
        lst = lst[stride:]
    return w


window = sliding_window_sums(lines)
inc = 0

for i, e in enumerate(window):
    if i == 0:
        if window[i + 1] > window[i]:
            inc += 1
    elif 0 < i < len(window) - 1:
        if window[i + 1] > window[i]:
            inc += 1

print(inc)
