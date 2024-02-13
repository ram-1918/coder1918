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
	fmt.Printf("\nType: %T, value: %v", y1, y1)
}
