package leetcode

import (
	"bufio"
	"fmt"
	"os"
)

func LoadDataStructures() {
	lst := []int{1, 2, 3, 4, 5, 6, 7}
	binary_search(lst, -1)
}

func ReadFileFromArgs() {
	counter := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counter)
	} else {
		for _, file := range files {
			f, err := os.Open(file)
			if err != nil {
				fmt.Fprintf(os.Stderr, "%v", err)
				continue
			}
			countLines(f, counter)
			f.Close()
		}
	}
	fmt.Println(files, counter)
	for line, v := range counter {
		if v > 1 {
			fmt.Println(line)
		}
	}
}

func countLines(f *os.File, counter map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		counter[input.Text()]++
	}
}
