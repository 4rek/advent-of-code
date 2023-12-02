package main

import (
	"strconv"
	"strings"
)

func Reverse(s []string) []string {
	var result []string = make([]string, 0)

	for i := len(s) - 1; i >= 0; i-- {
		result = append(result, s[i])
	}

	return result
}

func partOne(lines []string) int {
	result := 0

	for game, line := range lines {
		var maxColors map[string]int = map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}

		row := Reverse(strings.Split(line, " ")[2:])

		for idx, item := range row {
			key := strings.ReplaceAll(strings.ReplaceAll(strings.Trim(item, " "), ",", ""), ";", "")
			if idx%2 == 0 {
				val, _ := strconv.Atoi(row[idx+1])
				if val > maxColors[key] {
					maxColors[key] = val
				}
			}
		}

		if maxColors["red"] <= 12 && maxColors["green"] <= 13 && maxColors["blue"] <= 14 {
			result = result + game + 1
		}
	}

	return result
}

func partTwo(lines []string) int {
	result := 0

	for _, line := range lines {
		var maxColors map[string]int = map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}

		row := Reverse(strings.Split(line, " ")[2:])

		for idx, item := range row {
			key := strings.ReplaceAll(strings.ReplaceAll(strings.Trim(item, " "), ",", ""), ";", "")
			if idx%2 == 0 {
				val, _ := strconv.Atoi(row[idx+1])
				if val > maxColors[key] {
					maxColors[key] = val
				}
			}
		}

		result = result + maxColors["red"]*maxColors["green"]*maxColors["blue"]
	}

	return result
}
