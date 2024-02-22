package leetcode

import "fmt"

func binary_search(lst []int, target int) {
	fmt.Println("Executing Binary Search")
	fmt.Println("To perform Binary Search on Arrays, first the array has to be sorted")
	fmt.Printf("Given list: %v (sorted array) \nSearch Target: %d \n", lst, target)

	left, right := 0, len(lst)-1
	for left <= right {
		mid := (right-left)/2 + left
		if lst[mid] == target {
			fmt.Printf("Expected postion of target: %d \n", mid)
			return
		} else if lst[mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	fmt.Printf("Expected postion of target: %d \n", left)
}
