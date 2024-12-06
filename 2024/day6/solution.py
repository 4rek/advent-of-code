from typing import List, Set, Tuple
import os

def is_guard_in_grid(guard_position: Tuple[int, int], max_x: int, max_y: int) -> bool:
    x, y = guard_position
    return 0 <= x < max_x and 0 <= y < max_y

def move_guard(guard_position: Tuple[int, int], direction: str, obstacles: Set[Tuple[int, int]]) -> Tuple[Tuple[int, int], str]:
    x, y = guard_position

    if direction == "up":
        next_position = (x, y - 1)
        if next_position in obstacles:
            return guard_position, "right"
        return next_position, direction

    if direction == "right":
        next_position = (x + 1, y)
        if next_position in obstacles:
            return guard_position, "down"
        return next_position, direction

    if direction == "down":
        next_position = (x, y + 1)
        if next_position in obstacles:
            return guard_position, "left"
        return next_position, direction

    if direction == "left":
        next_position = (x - 1, y)
        if next_position in obstacles:
            return guard_position, "up"
        return next_position, direction

    return guard_position, direction

def get_visited_points(starting_position: Tuple[int, int], direction: str,
                       obstacles: Set[Tuple[int, int]], max_x: int, max_y: int) -> Tuple[Set[Tuple[int, int]], bool]:
    visited_states = set()
    visited_positions = set()
    guard_position = starting_position

    while is_guard_in_grid(guard_position, max_x, max_y):
        state = (guard_position, direction)
        if state in visited_states:
            return set(), True

        visited_states.add(state)
        visited_positions.add(guard_position)
        guard_position, direction = move_guard(guard_position, direction, obstacles)

    return visited_positions, False

def part1(lines: List[str]) -> int:
    max_y, max_x = len(lines), len(lines[0].strip())
    starting_position = (0, 0)
    direction = "up"
    obstacles = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == "^":
                starting_position = (x, y)
            elif char == "#":
                obstacles.add((x, y))

    visited, _ = get_visited_points(starting_position, direction, obstacles, max_x, max_y)
    return len(visited)

def part2(lines: List[str]) -> int:
    max_y, max_x = len(lines), len(lines[0].strip())
    obstacles = set()
    empty_positions = []

    starting_position = (0, 0)

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == '^':
                starting_position = (x, y)
            elif char == '#':
                obstacles.add((x, y))
            else:
                empty_positions.append((x, y))

    possibilities = 0

    for pos in empty_positions:
        if pos != starting_position:
            new_obstacles = obstacles | {pos}
            _, is_loop = get_visited_points(starting_position, "up", new_obstacles, max_x, max_y)
            if is_loop:
                possibilities += 1

    return possibilities

if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day6/inputs/main.txt", "r")
    lines = f.readlines()
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))
