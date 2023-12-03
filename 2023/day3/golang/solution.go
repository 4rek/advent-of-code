package main

import (
	"regexp"
	"strconv"
	"strings"
)

func partOne(lines []string) int {
	var results []int
	specialCharacters := "!@#$%^&*()-+?_=,<>/"

	for linesIdx, line := range lines {
		re := regexp.MustCompile(`\d+`)
		matches := re.FindAllStringIndex(line, -1)

		for _, match := range matches {
			x1 := max(match[0]-1, 0)
			x2 := min(match[1]+1, len(line))

			y1 := max(linesIdx-1, 0)
			y2 := min(linesIdx+1, len(lines)-1)

			checks := line[x1:x2]

			if y1 != linesIdx {
				checks += lines[y1][x1:x2]
			}

			if y2 != linesIdx {
				checks += lines[y2][x1:x2]
			}

			for _, char := range specialCharacters {
				if strings.Contains(checks, string(char)) {
					matchedVal, _ := strconv.Atoi(line[match[0]:match[1]])
					results = append(results, matchedVal)
				}
			}
		}
	}

	sum := 0
	for _, val := range results {
		sum += val
	}

	return sum
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func partTwo(lines []string) int {
	var results [][]string
	digitRegex := regexp.MustCompile(`\d+`)
	starRegex := regexp.MustCompile(`\*`)

	for linesIdx, line := range lines {
		for _, match := range digitRegex.FindAllStringIndex(line, -1) {
			x1 := max(match[0]-1, 0)
			x2 := min(match[1]+1, len(line))

			y1 := max(linesIdx-1, 0)
			y2 := min(linesIdx+1, len(lines)-1)

			checkAndAppend := func(y, x1, x2 int, matchValue string) {
				if starRegex.MatchString(lines[y][x1:x2]) {
					starIdx := -1
					for _, m := range starRegex.FindAllStringIndex(lines[y], -1) {
						if x1 <= m[0] && x2 >= m[1] {
							starIdx = m[0]
							break
						}
					}
					if starIdx != -1 {
						results = append(results, []string{strconv.Itoa(y) + strconv.Itoa(starIdx), matchValue})
					}
				}
			}

			matchValue := line[match[0]:match[1]]
			checkAndAppend(linesIdx, x1, x2, matchValue)

			if y1 != linesIdx {
				checkAndAppend(y1, x1, x2, matchValue)
			}

			if y2 != linesIdx {
				checkAndAppend(y2, x1, x2, matchValue)
			}
		}
	}

	dict := make(map[string][]int)
	for _, r := range results {
		key := r[0]
		value, _ := strconv.Atoi(r[1])
		dict[key] = append(dict[key], value)
	}

	res := 0
	for _, value := range dict {
		if len(value) == 2 {
			res += value[0] * value[1]
		}
	}

	return res
}
