from statistics import median

with open("input.txt", "r") as file_in:
    open_close = []
    for line in file_in:
        open_close.append(line.rstrip())

close_braces = ["}", "]", ">", ")"]
brace_matches = {"}": "{", "]": "[", ">": "<", ")": "("}
open_close_matches = {"{": "}", "[": "]", "<": ">", "(": ")"}
syntax_pts = {")": 3, "]": 57, "}": 1197, ">": 25137}
syntax_complete_pts = {")": 1, "]": 2, "}": 3, ">": 4}


def get_closing_mismatch(syntax_list):
    errors = []
    error_list = []
    open_incomplete = []
    for x in syntax_list:
        build_match = []
        for i, j in enumerate(x):
            # to check if a line starts with a closing brace
            if i == 0 and j in close_braces:
                errors.append(j)
                error_list.append(x)
                break
            build_match.append(j)
            if build_match[-1] in close_braces:
                match_close = brace_matches.get(build_match[-1])
                if match_close != build_match[-2]:
                    errors.append(j)
                    error_list.append(x)
                    break
                else:
                    build_match.pop()
                    build_match.pop()
        if not any([val for val in build_match if val in close_braces]):
            open_incomplete.append(
                list(reversed([open_close_matches.get(x) for x in build_match]))
            )
    return errors, open_incomplete


error_syntax, incomplete = get_closing_mismatch(open_close)

total_1 = 0
for err in error_syntax:
    total_1 += syntax_pts.get(err)

# part 1
print(total_1)


def incomplete_score_median(lst):
    score_aggr = []
    for x in lst:
        total_2 = 0
        for y in x:
            total_2 = total_2 * 5 + (syntax_complete_pts.get(y))
        score_aggr.append(total_2)
    return median(score_aggr)


# part 2
print(incomplete_score_median(incomplete))
