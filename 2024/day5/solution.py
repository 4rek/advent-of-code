from typing import List

import os

def is_line_correct(line: str, rules: dict):
    result = True

    line = list(map(int, line.split(",")))
    for idx, item in enumerate(line):
        rules_for_item = rules.get(item, [])
        if len(rules_for_item) == 0:
            continue

        for rule in rules_for_item:
            if rule in line and rule not in line[0:idx]:
                result = False

    return result

def part1(lines: List[str]):
    checking = False
    correct_lines = []
    rules = {}

    for line in lines:
        line = line.strip()

        if line == "":
            checking = True
            continue

        if checking:
            if is_line_correct(line, rules):
                correct_lines.append(list(map(int,line.split(','))))
        else:
            x = line.split("|")
            r = rules.get(int(x[1]), [])
            r.append(int(x[0]))
            rules[int(x[1])] = sorted(r)

    return sum(correct_line[len(correct_line)//2] for correct_line in correct_lines)

def custom_sort(list_to_reorder, rules):
    n = len(list_to_reorder)

    for i in range(n):
        for j in range(i + 1, n):
            if list_to_reorder[i] in rules and list_to_reorder[j] in rules[list_to_reorder[i]]:
                temp = list_to_reorder[i]
                list_to_reorder[i] = list_to_reorder[j]
                list_to_reorder[j] = temp

    return list_to_reorder

def part2(lines: List[str]):
    checking = False
    incorrect_lines = []
    rules = {}

    for line in lines:
        line = line.strip()

        if line == "":
            checking = True
            continue

        if checking:
            line_correct = is_line_correct(line, rules)
            if not line_correct:
                incorrect_lines.append(list(map(int,line.split(','))))
        else:
            x = line.split("|")
            r = rules.get(int(x[1]), [])
            r.append(int(x[0]))
            rules[int(x[1])] = sorted(r)

    corrected = []

    for line in incorrect_lines:
        corrected.append(custom_sort(line, rules))

    return sum(correct_line[len(correct_line)//2] for correct_line in corrected)


if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day5/inputs/main.txt", "r")
    lines = f.readlines()
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))
