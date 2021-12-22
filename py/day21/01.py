from itertools import cycle


def pos_after_die(pos, moves):
    t = (pos + moves) % 10
    return 10 if t == 0 else (pos + moves) % 10


def roll_die(p1_start, p2_start, target_sum):
    die = cycle(list(range(1, 101)))
    die_iter = iter(die)

    next_p1_pos, next_p2_pos = p1_start, p2_start
    p1_total, p2_total = 0, 0
    total_rolls = 0
    while True:
        p1_sum = 0
        for _ in range(3):
            total_rolls += 1
            p1_sum += next(die_iter)
        next_p1_pos = pos_after_die(next_p1_pos, p1_sum)
        p1_total += next_p1_pos
        if p1_total >= target_sum:
            total_sum = p2_total
            break

        p2_sum = 0
        for _ in range(3):
            total_rolls += 1
            p2_sum += next(die_iter)
        next_p2_pos = pos_after_die(next_p2_pos, p2_sum)
        p2_total += next_p2_pos
        if p2_total >= target_sum:
            total_sum = p1_total
            break
    return total_sum * total_rolls


# Part 1
print(roll_die(10, 2, 1000))


# Hard to really understand part 2, might give it a shot if I get more understanding.
