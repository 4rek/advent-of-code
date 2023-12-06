from functools import reduce


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
