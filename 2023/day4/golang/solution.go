package main

import (
	"fmt"
	"math"
	"strings"
	"time"

	"golang.org/x/exp/slices"
)

func partOne(lines []string) int {
	result := 0

	for _, line := range lines {
		local := -1

		numbers := strings.Split(strings.Split(line, ":")[1], "|")

		winning := slices.DeleteFunc(strings.Split(numbers[0], " "), func(e string) bool {
			return e == ""
		})
		having := slices.DeleteFunc(strings.Split(numbers[1], " "), func(e string) bool {
			return e == ""
		})

		for _, h := range having {
			if slices.Contains(winning, h) {
				local += 1
			}
		}

		if local > -1 {
			result += int(math.Pow(2, float64(local)))
		}
	}

	return result
}

func partTwo(lines []string) int {
	startTime := time.Now()
	d := make(map[int]int, len(lines))

	for i := range lines {
		d[i] = 0
	}

	for lineIdx, line := range lines {
		for i := 0; i <= d[lineIdx]; i++ {
			local := 0

			numbers := strings.Split(strings.Split(line, ":")[1], "|")

			winning := slices.DeleteFunc(strings.Split(numbers[0], " "), func(e string) bool {
				return e == ""
			})
			having := slices.DeleteFunc(strings.Split(numbers[1], " "), func(e string) bool {
				return e == ""
			})

			for _, h := range having {
				if slices.Contains(winning, h) {
					local += 1
				}
			}

			if local > 0 {
				for j := lineIdx + 1; j < lineIdx+1+local; j++ {
					d[j] += 1
				}
			}
		}
	}

	sum := 0

	for _, v := range d {
		sum += v
	}

	duration := time.Since(startTime)
	fmt.Println("time taken: ", duration)
	return sum + len(lines)
}
