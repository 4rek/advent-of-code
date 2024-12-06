from typing import List, Set, Tuple
import os

def is_guard_in_grid(guard_position, max_x, max_y):
    return guard_position[0] >= 0 and guard_position[0] < max_x and guard_position[1] >= 0 and guard_position[1] < max_y

def move_guard(guard_position, direction, obstacles):

    if direction == "up":
        if (guard_position[0], guard_position[1] - 1) in obstacles:
            direction = "right"
            return guard_position, direction
        else:
            return (guard_position[0], guard_position[1] - 1), direction

    if direction == "right":
        if (guard_position[0] + 1, guard_position[1]) in obstacles:
            direction = "down"
            return guard_position, direction
        else:
            return (guard_position[0] + 1, guard_position[1]), direction

    if direction == "down":
        if (guard_position[0], guard_position[1] + 1) in obstacles:
            direction = "left"
            return guard_position, direction
        else:
            return (guard_position[0], guard_position[1] + 1), direction

    if direction == "left":
        if (guard_position[0] - 1, guard_position[1]) in obstacles:
            direction = "up"
            return guard_position, direction
        else:
            return (guard_position[0] - 1, guard_position[1]), direction

    return guard_position, direction

def get_visited_points(starting_position: Tuple[int, int], direction: str, obstacles: Set[Tuple[int, int]], max_x: int, max_y: int) -> Tuple[Set[Tuple[int, int]], bool]:
    visited_states = []
    visited_positions = set()
    guard_position = starting_position

    max_steps = max_x * max_y * 4

    while is_guard_in_grid(guard_position, max_x, max_y) and len(visited_states) <= max_steps:
        state = (guard_position, direction)

        if state in visited_states:
            return set(), True

        visited_states.append(state)
        visited_positions.add(guard_position)

        guard_position, direction = move_guard(guard_position, direction, obstacles)

    return visited_positions, False


def part1(lines: List[str]):
    max_y = len(lines)
    max_x = len(lines[0])

    starting_position = (0, 0)
    direction = "up"
    obstacles = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == "^":
                starting_position = (x, y)
                break
            if char == "#":
                obstacles.append((x, y))

    visited, _ = get_visited_points(starting_position, direction, obstacles, max_x, max_y)

    return len(visited)

def part2(lines: List[str]):
    max_y = len(lines)
    max_x = len(lines[0])

    obstacles: Set[Tuple[int, int]] = set()
    empty_positions: Set[Tuple[int, int]] = set()

    starting_position = (0, 0)

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == '^':
                starting_position = (x, y)
            elif char == '#':
                obstacles.add((x, y))
            else:
                empty_positions.add((x, y))

    possibilities = set()

    for pos in empty_positions:
        if pos != starting_position:
            new_obstacles = obstacles | {pos}
            _, is_loop = get_visited_points(starting_position, "up", new_obstacles, max_x, max_y)
            if is_loop:
                possibilities.add(pos)

    print(possibilities)
    return len(possibilities)

if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day6/inputs/demo1.txt", "r")
    lines = f.readlines()
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))
