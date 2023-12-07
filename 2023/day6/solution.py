from functools import reduce
from math import sqrt


def part1(lines: str):
    times, distances = lines.split("\n")
    times = list(map(int, filter(len, times.split(":")[1].strip().split(" "))))
    distances = list(map(int, filter(len, distances.split(":")[1].strip().split(" "))))

    results = []
    for i in range(len(times)):
        local_results = sum(
            hold * (times[i] - hold) > distances[i] for hold in range(times[i])
        )
        results.append(local_results)

    return reduce((lambda x, y: x * y), results)


def part2(lines: str):
    times, distances = lines.split("\n")
    times = int("".join(filter(len, times.split(":")[1].strip().split(" "))))
    distance = int("".join(filter(len, distances.split(":")[1].strip().split(" "))))

    first_valid_i, low, high = 0, 0, times

    while low <= high:
        i = (high + low) // 2
        val = i * (times - i)

        if val > distance:
            first_valid_i = i
            high = i - 1
        else:
            low = i + 1

    return len(range(first_valid_i, times - first_valid_i + 1))


def solve_quadratic(b, c):
    c += 1e-6
    delta = b**2 - 4 * c

    if delta < 0:
        return None, None

    return int((-1 * b - sqrt(delta)) / 2), int((-1 * b + sqrt(delta)) / 2)


def part2_quadratic(lines: str):
    times, distances = lines.split("\n")
    times = int("".join(filter(len, times.split(":")[1].strip().split(" "))))
    distance = int("".join(filter(len, distances.split(":")[1].strip().split(" "))))

    x1, x2 = solve_quadratic(times, distance)
    return int(abs(x1) - abs(x2))


# def main():
#     time_start = process_time_ns()
#     f = open(f"{os.getcwd()}/day6/inputs/demo.txt", "r")
#     lines = f.read().strip()
#     # answer = part2(lines)
#     answer = part2_quadratic(lines)
#     time_end = process_time_ns()
#     time_duration = time_end - time_start
#     print(f"Took {time_duration} ns")


# main()
