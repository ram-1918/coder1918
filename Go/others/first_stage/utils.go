package main

import "fmt"

func useArrays() {
	/*
		Create:
			var array_name = [length]type{values}
			var array_name = [...]type{values}
			array_name := make([]type, length, capacity)
			// Slice inside a slice
			array_name_2d := [][]type{
				[]type{values},
				[]type{values},
			}
		Read:
			value_at_index = array_name[index]
		Update:
			array_name[index] = newvalue
		Delete ???
			array_name[index]
		Slice:
			// Slices doesn't store any data, they just describes a section of an underlying array
			// Slice literal is same as the array literal but without the length
			slice_name = array_name[start: end]
			var slice_name = []type{} // Empty slice
			var slice_name = []type{1,2,3} // slice with values
			var slice_name []type // another way
			var slice_name []type = original_array[1:4]
		Append:
			// First argument of append should be a slice
			slice_name = append(slice_name, value1, value2...)
			slice_name = append(slice_name, slice_name2...) // ... is required to append another slice(kind of spread operator)
		Copy:
			copy(dest, src) // create an empty slice of length 'src'
		Length, Capacity:
			n := len(arr)
			len() => end - start
			cap() => n - start
		nil slice:
			length and capacity => 0

	*/
	fmt.Println("--------Arrays--------")
	// Array declaration - 1
	// var array_name = [length]type{values}
	var arr1 = [4]int{1, 2, 3} // partially initialized while declaration
	fmt.Printf("arr1: %v, length: %d, capacity: %d\n", arr1, len(arr1), cap(arr1))
	arr2 := [...]int{4, 5, 6}
	fmt.Printf("arr2: %v, length: %d, capacity: %d\n", arr2, len(arr2), cap(arr2))
	var arr3 = []int{}
	fmt.Printf("arr3: %v, length: %d, capacity: %d\n", arr3, len(arr3), cap(arr3))
	arr3 = append(arr3, 4, 1, 3)
	fmt.Printf("arr3: %v, length: %d, capacity: %d\n", arr3, len(arr3), cap(arr3))
	var arr4 []int
	fmt.Println("array4 ", arr4)
	// sort.Slice(arr3, func(i, j int) bool {

	// })
	fmt.Printf("First: %v, Last: %v, reverse?: %v, sort?: %v\n", arr3[0], arr3[len(arr3)-1], arr3, arr3)

	twod := [][]string{
		[]string{"a", "b"},
	}
	fmt.Println(twod, twod[0])
}

func useConditions() {
	fmt.Println("--------Conditionals--------")
	fmt.Println("------if/else-----")
	val := 5
	if val > 5 {
		fmt.Println("Value is greater than the thresold")
	} else if val == 5 {
		fmt.Println("Thresold requirement met")
	} else {
		fmt.Println("Thresold requirement not met")
	}
	fmt.Println("------switch case/multi-value switch case-----")
	switch val + 7 {
	case 5, 10, 15:
		{
			fmt.Println("Val is multiple of 5")
		}
	case 6, 12, 18:
		{
			fmt.Println("Val is multiple of 6")
		}
	default:
		{
			fmt.Println("Default case reached")
		}
	}
}

func useLoops() {
	fmt.Println("--------For Loop--------")
	// For loop is the only loop in Go
	fmt.Println("--------Generic For Loop--------")
	// Var declaration is not allowed in for initializer
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}
	fmt.Println("--------Nested For Loop--------")
	for i := 0; i < 3; i++ {
		for j := i; j < 3; j++ {
			fmt.Println(i, j)
		}
	}

	arr := [...]int{10, 20, 30, 40, 50}
	var n int = len(arr)

	fmt.Println("--------For Loop for Arrays based on length--------")
	for i := 0; i < n; i++ {
		fmt.Printf("index: %v, Value: %v\n", i, arr[i])
	}
	fmt.Println("--------For Loop for Arrays with range--------")
	for idx, value := range arr {
		fmt.Printf("index: %v, Value: %v\n", idx, value)
	}
	fmt.Println("--------For Loop to behave like a while loop--------")
	for i := 0; i == i; i++ {
		if i == 3 {
			fmt.Println("Termination condition")
			break
		}
		fmt.Println(i)
	}
	sum, title := sumOfNums(1, 2, "Sum")
	fmt.Println(title, sum)
}

// Named return function
func sumOfNums(a int, b int, c string) (result int, title string) {
	result = a + b // or result := a + b + c
	title = c + " of Numbers"
	return result, title
}

// Recurssion
func counter(x int) int {
	if x == 5 {
		fmt.Println("Recurssion terminated")
		return 0
	}
	fmt.Println("Recurrsion in progress... ", x)
	return counter(x + 1)
}

func getFactorial(x float32) (result float32) {
	if x <= 0 {
		result = 1
	} else {
		result = x * getFactorial(x-1)
	}
	return
}
