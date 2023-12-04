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
    d = {}

    for i in range(0, len(lines)):
        d[i] = {"wins": 0, "count": 1}

    for line_idx, line in enumerate(lines):        
        local_result = 0
        numbers = line.strip().split(":")[1].strip().split('|')
        winning = list(filter(len, numbers[0].strip().split(" ")))
        having = list(filter(len, numbers[1].strip().split(" ")))

        for h in having:
            if h in winning:
                local_result += 1

        d[line_idx]["wins"] = local_result
    
    s = 0

    for key, value in d.items():
        for x in range(key+1, key + 1 + value["wins"]):
            d[x]["count"] += 1 * value["count"]
        s += value["count"]

    return s

if __name__ == "__main__":
    f = open(os.getcwd() + '/day4/inputs/main.txt', 'r')
    lines = f.readlines()
    print(part2(lines))