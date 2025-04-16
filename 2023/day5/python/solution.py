from typing import List
import os


class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def intersection(self, other):
        tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
        return tmp if tmp.lower < tmp.upper else None

    def subtract(self, other):
        ins = self.intersection(other)
        if ins is None:
            # ----------
            #    			---
            return [Range(self.lower, self.upper)]
        elif (ins.lower, ins.upper) == (self.lower, self.upper):
            #    -----		intersect
            #    -----		self
            return []
        elif ins.lower == self.lower:
            #    --			intersect
            #    -----		self
            return [Range(ins.upper, self.upper)]
        elif ins.upper == self.upper:
            #       --		intersect
            #    -----		self
            return [Range(self.lower, ins.lower)]
        else:
            #      --		intersect
            #    ------		self
            return [Range(self.lower, ins.lower), Range(ins.upper, self.upper)]

    def add(self, offset):
        return Range(self.lower + offset, self.upper + offset)


class PartTwoSolver:
    def __init__(self, maps):
        self.maps = maps
        self.result = float("inf")

    def solve_recursively(self, r: Range, layer: int):
        if layer == len(self.maps):
            self.result = min(self.result, r.lower)
            return
        for destination, source, steps in self.maps[layer].rules:
            map_r = Range(source, source + steps)
            ins = r.intersection(map_r)
            if ins is not None:
                self.solve_recursively(ins.add(destination - source), layer + 1)
                sub = r.subtract(map_r)
                if len(sub) == 0:
                    return
                r = sub[0]
                if len(sub) == 2:
                    self.solve_recursively(sub[1], layer)
        self.solve_recursively(r, layer + 1)


class Mapa:
    def __init__(self, strs: List[str]) -> None:
        self.rules = []
        for s in strs.splitlines()[1:]:
            destination, source, steps = map(int, s.split())
            self.rules.append((destination, source, steps))

    def transform(self, value) -> str:
        return next(
            (
                destination + value - source
                for destination, source, steps in self.rules
                if source <= value < source + steps
            ),
            value,
        )


def part1(lines: str):
    seeds, *maps = lines.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))
    maps = list(map(Mapa, maps))

    locations = []
    for s in seeds:
        for m in maps:
            s = m.transform(s)
        locations.append(s)

    return min(locations)


def part2(lines: str):
    seeds, *maps = lines.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))
    maps = list(map(Mapa, maps))

    solver = PartTwoSolver(maps)

    for i in range(0, len(seeds), 2):
        solver.solve_recursively(Range(seeds[i], seeds[i] + seeds[i + 1]), 0)

    return solver.result
