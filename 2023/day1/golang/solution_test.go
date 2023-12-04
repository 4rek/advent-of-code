package main

import (
	"fmt"
	"os"
	"strings"
	"testing"
	"time"
)

func TestDay2(t *testing.T) {
	answers := []int{142, 54304, 281, 54418}

	t1 := time.Now()
	demoData, err := os.ReadFile("../inputs/demo1.txt")
	if err != nil {
		panic(err)
	}
	demo2Data, err := os.ReadFile("../inputs/demo2.txt")
	if err != nil {
		panic(err)
	}
	mainData, err := os.ReadFile("../inputs/main.txt")
	if err != nil {
		panic(err)
	}

	demoLines := strings.Split(string(demoData), "\n")
	demo2Lines := strings.Split(string(demo2Data), "\n")
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
		ans := partTwo(demo2Lines)
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
