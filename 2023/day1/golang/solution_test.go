package main

import (
	"os"
	"strings"
	"testing"
)

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

	t.Run("Runs with demo input", func(t *testing.T) {
		ans := partOne(demoLines)

		if ans != 142 {
			t.Errorf("got %d, want %d", ans, 142)
		}
	})
	t.Run("Runs with main input", func(t *testing.T) {
		ans := partOne(mainLines)
		if ans != 54304 {
			t.Errorf("got %d, want %d", ans, 54304)
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

	t.Run("Runs with demo input", func(t *testing.T) {
		ans := partTwo(demoLines)

		if ans != 281 {
			t.Errorf("got %d, want %d", ans, 281)
		}
	})
	t.Run("Runs with main input", func(t *testing.T) {
		ans := partTwo(mainLines)
		if ans != 54418 {
			t.Errorf("got %d, want %d", ans, 54418)
		}
	})
}
