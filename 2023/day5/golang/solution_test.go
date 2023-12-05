package main

import (
	"fmt"
	"os"
	"testing"
	"time"
)

func TestDay5(t *testing.T) {
	answers := []int{13, 24175, 30, 18846301}

	t1 := time.Now()
	demoData, err := os.ReadFile("../inputs/demo1.txt")
	if err != nil {
		panic(err)
	}
	mainData, err := os.ReadFile("../inputs/main.txt")
	if err != nil {
		panic(err)
	}

	fmt.Println("Time to read files: ", time.Since(t1))

	t.Run("Part one - demo input", func(t *testing.T) {
		tt := time.Now()
		ans := partOne(string(demoData))
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[0] {
			t.Errorf("got %d, want %d", ans, answers[0])
		}
	})
	t.Run("Part one - main input", func(t *testing.T) {
		tt := time.Now()
		ans := partOne(string(mainData))
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[1] {
			t.Errorf("got %d, want %d", ans, answers[1])
		}
	})
	t.Run("Part two - demo input", func(t *testing.T) {
		tt := time.Now()
		ans := partTwo(string(demoData))
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[2] {
			t.Errorf("got %d, want %d", ans, answers[2])
		}
	})
	t.Run("Part two - main input", func(t *testing.T) {
		tt := time.Now()
		ans := partTwo(string(mainData))
		fmt.Println("Time to run: ", time.Since(tt))
		if ans != answers[3] {
			t.Errorf("got %d, want %d", ans, answers[3])
		}
	})
}
