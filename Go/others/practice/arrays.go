package practice

import "fmt"

func Arrays() {
	fmt.Println("---------arrays next-level-----------")
	// Declaration

	// var n int = 5
	// var arrayName [n]int // raises an error: invalid length n

	var arrayName [2]int
	arrayName[0] = 1
	arrayName[1] = 2
	// arrayName[2] = 3 // Outofbounds
	fmt.Println(arrayName, len(arrayName), cap(arrayName))
	// There are many slices utility functions like slices.Equal(slice1, slice2)
	var sliceName = arrayName[:]
	// A slice references the storage of the array behind scenes
	var arrayName2 = make([]int, 0, 1)
	arrayName2 = append(arrayName2, 10, 20)
	fmt.Println(sliceName, arrayName2, len(arrayName2), cap(arrayName2))
	var twod [2][2]int
	var twodSliceInit = [][]int{{1, 2}, {3, 4}}
	var twodSlice = make([][]int, 3)
	twodSlice[0] = append(twodSlice[0], 3)
	twodSlice[1] = append(twodSlice[1], 4)
	fmt.Println(twod, twodSliceInit, twodSlice)
}
