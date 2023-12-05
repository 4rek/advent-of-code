package main

import (
	"fmt"
	"os"
)

func partOne(lines string) int {
	// @TODO: Implement

	return 22
}

func partTwo(lines string) int {
	// TODO: Implement
	return 33
}

func main() {
	d, err := os.ReadFile("../inputs/main.txt")
	if err != nil {
		panic(err)
	}

	fmt.Println("Part one demo: ", partOne(string(d)))

}
