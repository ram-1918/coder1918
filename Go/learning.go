// Every program is a part of a package
// In Go, any executable code belongs to the main package

package main // This program(learning.go) belongs to the main package
import (
	"fmt"
) // Imports files that are included in 'fmt' package

var MAX_INT int = 120344
var a = 10

// Constants declared may or may not be used
const (
	const1 string = "RAM"
	const2 int    = 234
)

// any code inside curley braces will be executed
func main() {
	// Variables are declared but not initialized; if this is the case type has to be specified
	// This is helpful when their initial values are unknown
	// Can be declared and initialized inside/outside a function
	// Declared variables/constants/packages has to be USED
	// We can redeclare already declared variables
	fmt.Println("Learning Go") // Println() function made available from 'fmt' package
	// Variable declaration
	var id int
	var test = 12
	var student, dept string = "fre", "CSE" // Multi-line declaration
	// Block Declaration
	var (
		a int
		b string = "var b"
		c bool   = false
	)
	id, student = 123, "ram" // multi-line variable assignment
	sumbission_count := 12   // Has to be declared inside a function
	fmt.Println(student, id, sumbission_count, MAX_INT, a, b, c, test, dept)
	fmt.Print(const1, " ", const2, "\n")
	fmt.Printf("percent v is to print value of args, ex: %v \npercent T is to print the type of args, ex: %T", a, a)

	// Data Types in detail
	var x uint = 500
	var y int64 = 1270
	fmt.Printf("\nType: %T, value: %v", x, x)
	fmt.Printf("\nType: %T, value: %v", y, y)

	var x1 float32 = 52.23001
	var y1 float64 = 32.4e+302
	fmt.Printf("\nType: %T, value: %v", x1, x1)
	fmt.Printf("\nType: %T, value: %v\n", y1, y1)

	// Function calls
	use_arrays()
	use_conditions()
	use_loops()
}

func use_arrays() {
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
	// sort.Slice(arr3, func(i, j int) bool {

	// })
	fmt.Printf("First: %v, Last: %v, reverse?: %v, sort?: %v\n", arr3[0], arr3[len(arr3)-1], arr3, arr3)
}

func use_conditions() {
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

func use_loops() {
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

}
