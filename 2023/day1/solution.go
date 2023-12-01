package main

import (
	"fmt"
	"regexp"
	"sort"
	"strconv"
)

type Result struct {
	index int
	value string
}

func partOne(lines []string) int {
	var results []int = make([]int, 0)

	for _, line := range lines {
		var localResults []Result = make([]Result, 0)
		for i, char := range line {
			numeric := regexp.MustCompile(`\d`).MatchString(string(char))

			if numeric {
				localResults = append(localResults, Result{index: i, value: string(char)})
			}
		}

		num, _ := strconv.Atoi(localResults[0].value + localResults[len(localResults)-1].value)
		results = append(results, num)
	}

	fmt.Println(results)

	var sum int = 0

	for _, result := range results {
		sum += result
	}

	return sum
}

func partTwo(lines []string) int {
	var results []int = make([]int, 0)
	var numsDict map[string]string = map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	for _, line := range lines {
		var localResults []Result = make([]Result, 0)
		for i, char := range line {
			numeric := regexp.MustCompile(`\d`).MatchString(string(char))

			if numeric {
				localResults = append(localResults, Result{index: i, value: string(char)})
			}
		}

		for key, value := range numsDict {
			re := regexp.MustCompile(key)
			matches := re.FindAllStringIndex(line, -1)
			for _, match := range matches {
				localResults = append(localResults, Result{match[0], value})
			}
		}

		sort.Slice(localResults[:], func(i, j int) bool {
			return localResults[i].index < localResults[j].index
		})

		num, _ := strconv.Atoi(localResults[0].value + localResults[len(localResults)-1].value)
		results = append(results, num)
	}

	fmt.Println(results)

	var sum int = 0

	for _, result := range results {
		sum += result
	}

	return sum
}
