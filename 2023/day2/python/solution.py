from typing import List
import os

def part1(lines: List[str]):
    results = 0
    for game, line in enumerate(lines):
        max_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        row = line.split(' ')[2:][::-1]
        
        for idx, item in enumerate(row):
            i = item.strip().replace(',', '').replace(';', '')
            if idx % 2 == 0:
                v = int(row[idx+1])
                max_colors[i] = v if max_colors[i] < v else max_colors[i];

        if max_colors["red"] <= 12 and max_colors["green"] <= 13 and max_colors["blue"] <= 14:
            results = results + game + 1
            
    return results

def part2(lines: List[str]):
    result = 0
    for line in lines:
        max_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        row = line.split(' ')[2:][::-1]
        
        for idx, item in enumerate(row):
            i = item.strip().replace(',', '').replace(';', '')
            if idx % 2 == 0:
                v = int(row[idx+1])
                max_colors[i] = v if max_colors[i] < v else max_colors[i];

        result += max_colors["red"] * max_colors["green"] * max_colors["blue"]
            
    return result


if __name__ == "__main__":
    f = open(os.getcwd() + '/day2/inputs/demo2.txt', 'r')
    lines = f.readlines()
    part2(lines)