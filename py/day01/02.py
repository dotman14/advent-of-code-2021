with open('/Users/oyesanmi/PycharmProjects/advent-of-code-2021/py/day01/puzzle_input.txt', 'r') as file_in:
    lines_list = [int(lines.rstrip()) for lines in file_in]

inc = 0


def sliding_window_sums(lst, window_size=3, stride=1):
    """ Return a list of sums of sliding window"""
    w = []
    while lst:
        if len(lst[:window_size]) == window_size:
            w.append(sum(lst[:window_size]))
        lst = lst[stride:]
    return w


window = sliding_window_sums(lines_list)

for i, e in enumerate(window):
    if i == 0:
        if window[i + 1] > window[i]:
            inc += 1
    elif 0 < i < len(window) - 1:
        if window[i + 1] > window[i]:
            inc += 1

print(inc)