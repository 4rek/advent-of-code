package main

import (
	"os"
	"strings"
	"testing"
)

var day string = "Day 2 "

func TestPartOne(t *testing.T) {
	demoData, err := os.ReadFile("../inputs/demo1.txt")

	if err != nil {
		panic(err)
	}

	mainData, err := os.ReadFile("../inputs/main.txt")

	if err != nil {
		panic(err)
	}

	demoLines := strings.Split(string(demoData), "\n")
	mainLines := strings.Split(string(mainData), "\n")

	t.Run(day+"Runs with demo input", func(t *testing.T) {
		ans := partOne(demoLines)

		if ans != 8 {
			t.Errorf("got %d, want %d", ans, 8)
		}
	})
	t.Run(day+"Runs with main input", func(t *testing.T) {
		ans := partOne(mainLines)
		if ans != 2076 {
			t.Errorf("got %d, want %d", ans, 2076)
		}
	})
}

func TestPartTwo(t *testing.T) {
	demoData, err := os.ReadFile("../inputs/demo2.txt")

	if err != nil {
		panic(err)
	}

	mainData, err := os.ReadFile("../inputs/main.txt")

	if err != nil {
		panic(err)
	}

	demoLines := strings.Split(string(demoData), "\n")
	mainLines := strings.Split(string(mainData), "\n")

	t.Run(day+"Runs with demo input", func(t *testing.T) {
		ans := partTwo(demoLines)

		if ans != 2286 {
			t.Errorf("got %d, want %d", ans, 2286)
		}
	})
	t.Run(day+"Runs with main input", func(t *testing.T) {
		ans := partTwo(mainLines)
		if ans != 70950 {
			t.Errorf("got %d, want %d", ans, 70950)
		}
	})
}
