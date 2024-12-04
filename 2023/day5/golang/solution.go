package main

import (
	"strconv"
	"strings"
)

func parseNumbers(s string) []int {
	svalues := strings.Split(s, " ")
	numbers := make([]int, len(svalues))
	for i, s := range svalues {
		numbers[i], _ = strconv.Atoi(s)
	}
	return numbers
}

func transform(source int, rules [][]int) int {
	for _, rule := range rules {
		if source >= rule[1] && source < rule[1]+rule[2] {
			return rule[0] + source - rule[1]
		}
	}

	return source
}

func reverse(dest int, rules [][]int) int {
	var source int
	for _, rule := range rules {
		source = dest + rule[1] - rule[0]
		if source >= rule[1] && source < rule[1]+rule[2] {
			return source
		}
	}

	return dest
}

func partOne(input string) int {
	lines := strings.Split(input, "\n")
	seeds := parseNumbers(lines[0][strings.Index(lines[0], ": ")+2:])
	s := 0

	translators := make([][][]int, 0, 8)
	translators = append(translators, make([][]int, 0, 8))
	for i := 3; i < len(lines); i++ {
		// on every empty line, start a new map
		if lines[i] == "" {
			i += 1
			s += 1
			translators = append(translators, make([][]int, 0, 8))
			continue
		}

		translators[s] = append(translators[s], parseNumbers(lines[i]))
	}

	result := 1 << 31
	for _, seed := range seeds {
		for _, t := range translators {
			seed = transform(seed, t)
		}
		if seed < result {
			result = seed
		}
	}

	return result
}

func partTwo(input string) int {
	lines := strings.Split(input, "\n")
	seeds := parseNumbers(lines[0][strings.Index(lines[0], ": ")+2:])
	s := 0

	translators := make([][][]int, 0, 8)
	translators = append(translators, make([][]int, 0, 8))
	for i := 3; i < len(lines); i++ {
		// on every empty line, start a new map
		if lines[i] == "" {
			i += 1
			s += 1
			translators = append(translators, make([][]int, 0, 8))
			continue
		}

		translators[s] = append(translators[s], parseNumbers(lines[i]))
	}

	var x int
	var l int
	for {
		x = l
		for i := len(translators) - 1; i >= 0; i-- {
			x = reverse(s, translators[i])
		}

		// check if s is valid seed number
		for i := 0; i < len(seeds); i += 2 {
			if x > seeds[i] && x < seeds[i]+seeds[i+1] {
				return l
			}
		}

		l++
	}
}
