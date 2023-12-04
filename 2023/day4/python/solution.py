from typing import List
import os

def part1(lines: List[str]):
    result = 0
    for line in lines:
        local_result = -1

        numbers = line.strip().split(":")[1].strip().split('|')
        winning = list(filter(len, numbers[0].strip().split(" ")))
        having = list(filter(len, numbers[1].strip().split(" ")))

        for h in having:
            if h in winning:
                local_result += 1
        
        if local_result > -1:
            result += 2 ** (local_result)

    return result

def part2(lines: List[str]):
    d = { i: 0 for i in range(0, len(lines))}

    for line_idx, line in enumerate(lines):        
        for _ in range(0, d[line_idx] + 1):
            local_result = 0
            numbers = line.strip().split(":")[1].strip().split('|')
            winning = list(filter(len, numbers[0].strip().split(" ")))
            having = list(filter(len, numbers[1].strip().split(" ")))

            for h in having:
                if h in winning:
                    local_result += 1

            if local_result > 0:
                for x in range(line_idx+1, line_idx + 1 + local_result):
                    d[x] += 1

    return sum(d.values()) + len(lines)


if __name__ == "__main__":
    f = open(os.getcwd() + '/day4/inputs/main.txt', 'r')
    lines = f.readlines()
    part2(lines)