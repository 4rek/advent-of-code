from typing import List
import os
import re

special_characters = "!@#$%^&*()-+?_=,<>/"


def part1(lines: List[str]):
    results = []

    for lines_idx, line in enumerate(lines):
        for match in re.finditer(r"\d+", line.strip()):
            x1 = match.start() - 1 if match.start() > 0 else 0
            x2 = match.end() + 1 if match.end() < len(line) - 1 else len(line) - 1

            y1 = lines_idx - 1 if lines_idx > 0 else 0
            y2 = lines_idx + 1 if lines_idx < len(lines) - 1 else len(lines) - 1

            checks = line[x1:x2]

            if y1 is not lines_idx:
                checks += lines[y1][x1:x2]

            if y2 is not lines_idx:
                checks += lines[y2][x1:x2]

            results.extend(match.group() for i in special_characters if i in checks)
    results = list(map(lambda x: int(x), results))
    return sum(results)


def part2(lines: List[str]):
    results = []

    for lines_idx, line in enumerate(lines):
        for match in re.finditer(r"\d+", line.strip()):
            x1 = match.start() - 1 if match.start() > 0 else 0
            x2 = match.end() + 1 if match.end() < len(line) - 1 else len(line) - 1

            y1 = lines_idx - 1 if lines_idx > 0 else 0
            y2 = lines_idx + 1 if lines_idx < len(lines) - 1 else len(lines) - 1

            if "*" in line[x1:x2]:
                star_idx = -1
                for m in re.finditer(r"\*", line):
                    if x1 <= m.start() and x2 >= m.end():
                        star_idx = m.start()
                results.append([str(lines_idx) + str(star_idx), int(match.group())])

            if y1 is not lines_idx and "*" in lines[y1][x1:x2]:
                star_idx = -1
                for m in re.finditer(r"\*", lines[y1]):
                    if x1 <= m.start() and x2 >= m.end():
                        star_idx = m.start()
                results.append([str(y1) + str(star_idx), int(match.group())])

            if y2 is not lines_idx and "*" in lines[y2][x1:x2]:
                star_idx = -1
                for m in re.finditer(r"\*", lines[y2]):
                    if x1 <= m.start() and x2 >= m.end():
                        star_idx = m.start()
                results.append([str(y2) + str(star_idx), int(match.group())])

    d = {}
    for r in results:
        if r[0] in d:
            d[r[0]].append(r[1])
        else:
            d[r[0]] = [r[1]]

    return sum(value[0] * value[1] for value in d.values() if len(value) == 2)
