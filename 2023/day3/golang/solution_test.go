package main

import (
	"fmt"
	"os"
	"strings"
	"testing"
	"time"
)

func TestDay3(t *testing.T) {
	answers := []int{4361, 527364, 467835, 79026871}

	t1 := time.Now()
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

	fmt.Println("Time to read files: ", time.Since(t1))

	t.Run("Part one - demo input", func(t *testing.T) {
		tt := time.Now()
		ans := partOne(demoLines)
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[0] {
			t.Errorf("got %d, want %d", ans, answers[0])
		}
	})
	t.Run("Part one - main input", func(t *testing.T) {
		tt := time.Now()
		ans := partOne(mainLines)
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[1] {
			t.Errorf("got %d, want %d", ans, answers[1])
		}
	})
	t.Run("Part two - demo input", func(t *testing.T) {
		tt := time.Now()
		ans := partTwo(demoLines)
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[2] {
			t.Errorf("got %d, want %d", ans, answers[2])
		}
	})
	t.Run("Part two - main input", func(t *testing.T) {
		tt := time.Now()
		ans := partTwo(mainLines)
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[3] {
			t.Errorf("got %d, want %d", ans, answers[3])
		}
	})
}
