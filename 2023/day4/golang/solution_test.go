package main

import (
	"os"
	"strings"
	"testing"
)

var day string = "Day 4 "

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

		if ans != 13 {
			t.Errorf("got %d, want %d", ans, 13)
		}
	})
	t.Run(day+"Runs with main input", func(t *testing.T) {
		ans := partOne(mainLines)
		if ans != 24175 {
			t.Errorf("got %d, want %d", ans, 24175)
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

		if ans != 30 {
			t.Errorf("got %d, want %d", ans, 30)
		}
	})
	t.Run(day+"Runs with main input", func(t *testing.T) {
		ans := partTwo(mainLines)
		if ans != 18846301 {
			t.Errorf("got %d, want %d", ans, 18846301)
		}
	})
}
