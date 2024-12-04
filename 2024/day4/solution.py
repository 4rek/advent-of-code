from typing import List

import os


def part1(lines: List[str]):
    count = 0
    max_y = len(lines)
    max_x = len(lines[0].strip())

    for y, line in enumerate(lines):
        for x, ch in enumerate(line.strip()): 
            if ch == "X":
                # to right
                if (line[x:x+4] == "XMAS"):
                    count += 1
                    
                #to left
                if (line[x-3:x+1] == "SAMX"):
                    count += 1
                    
                #to bottom
                if (y+3 < max_y and lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == "XMAS"):
                    count += 1
                
                # to top
                if (y-3 >= 0 and lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == "XMAS"):
                    count += 1

                # diagonal bottom-right
                if (y+3 < max_y and x+3 < max_x and lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3] == "XMAS"):
                    count += 1
                
                # diagonal bottom-left
                if (y+3 < max_y and x-3 >= 0 and lines[y][x] + lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3] == "XMAS"):
                    count += 1
                
                # diagonal top-right
                if (y-3 >= 0 and x+3 < max_x and lines[y][x] + lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3] == "XMAS"):
                    count += 1
                
                # diagonal top-left
                if (y-3 >= 0 and x-3 >= 0 and lines[y][x] + lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3] == "XMAS"):
                    count += 1
    return count

def part2(lines: List[str]):
    count = 0
    max_y = len(lines)
    max_x = len(lines[0].strip())

    for y, line in enumerate(lines):
        for x, ch in enumerate(line.strip()): 
            if ch == "A" and x-1 >= 0 and x+1 < max_x and y-1 >= 0 and y+1 < max_y:
                q = lines[y-1][x-1] + lines[y-1][x+1] + lines[y+1][x-1] + lines[y+1][x+1]
                if q in ["MMSS", "SSMM", "MSMS", "SMSM"]:
                    count += 1

    return count


if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day4/inputs/main.txt", "r")
    lines = f.readlines()
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))