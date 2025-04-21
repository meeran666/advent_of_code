package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "example amp string amp example"
	substring := "amp"
	start := 0
	var indices []int

	for {
		fmt.Println("start")
		fmt.Println(start)
		idx := strings.Index(str[start:], substring)
		fmt.Println("idx")
		fmt.Println(idx)
		if idx == -1 {
			break
		}
		actualPos := start + idx

		indices = append(indices, actualPos)
		start = actualPos + len(substring)
	}

	fmt.Println("All occurrences at positions:", indices)
}
