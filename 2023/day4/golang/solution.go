package main

import (
	"fmt"
	"math"
	"sort"
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

type Cart struct {
	Wins  int
	Count int
}

func partTwo(lines []string) int {
	startTime := time.Now()
	d := make(map[int]Cart, len(lines))

	for i := range lines {
		d[i] = Cart{0, 1}
	}

	for lineIdx, line := range lines {
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
			d[lineIdx] = Cart{local, 1}
		}

	}

	sum := 0

	keys := make([]int, 0, len(d))
	for k := range d {
		keys = append(keys, k)
	}

	sort.Ints(keys) // Sort the keys

	for _, k := range keys {
		for i := k + 1; i < k+1+d[k].Wins; i++ {
			c := d[i]
			d[i] = Cart{c.Wins, c.Count + 1*d[k].Count}
		}
		sum += d[k].Count
	}

	duration := time.Since(startTime)
	fmt.Println("time taken: ", duration)
	return sum
}
