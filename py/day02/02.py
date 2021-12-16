def str_to_tuple(str: str) -> list:
    pos_int = str.split(" ")
    return [pos_int[0], int(pos_int[1])]


with open("input.txt", "r") as file_in:
    l = [str_to_tuple(lines.rstrip()) for lines in file_in]


def get_position(pos_lst: list) -> int:
    x, y, a = 0, 0, 0
    for pos in pos_lst:
        if pos[0] == "down":
            a += pos[1]
        if pos[0] == "up":
            a -= pos[1]
        if pos[0] == "forward":
            x += pos[1]
            y += a * pos[1]
    return abs(x * y)


print(get_position(l))
