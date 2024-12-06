package practice

import "fmt"

/**
Template:
func functionName(parameters) returnType {
	// Statements
}

Types:
	Named: Normal function that wraps the logic
	Anonymous: Functions without a name, mainly used in callbacks and inline functions
	Methods: attached to structs operating on the data within the function

> Use blank identifier, if only a multiple subset of returned values are needed
> Variadic number of arguments, for example, function(slice ...int). Now slice containes arguments passed to the function
> 	while passing to a function, push all the values to a slice, and pass the slice to the function by calling it as function(slice...)
> Closures: (also used as inline functions)
	1. These are the powerful feature in Go, they allow functions to remember the environement they were created,
	even after the environemnt goes out of scope.
	2. It has the ability to hold onto the external state
	3. Closures can also be recursive, but this requires the closure to be declared with a typed var explicitly before it’s defined.
>


*/

// Closure Example 1
func closureFunc() func() int {
	i := 0
	fmt.Println("caputed var ", i)
	return func() int {
		i++
		return i
	}
}

// Closure Example 2
func isLoggedIn() func() bool {
	isLoggedin := true
	return func() bool {
		return isLoggedin
	}
}

func factorial(n int) int {
	if n == 1 {
		return 1
	}
	return n * factorial((n - 1))
}

func Functions(nums ...int) (int, int, int, int) {
	fmt.Println("------------Functions-----------")
	// Start with a capital letter to export
	fmt.Println("Arguments: ", nums)

	closureVar := closureFunc()                    // It returns the inner function, which is attached to a variable
	fmt.Println("Invoked a Closure", closureVar()) // we are calling the inner function there after
	fmt.Println("Invoked a Closure", closureVar()) // The question here is that how is it maintaing the state ???

	user := isLoggedIn()
	fmt.Println("is Loggedin", user())
	fmt.Println("is Loggedin", user())

	fmt.Println("Recurssion example: Factorial of 3: ", factorial(3))

	var fibnocciClosure func(n int) int // Declare the closure function before using that function for recurssion

	fibnocciClosure = func(n int) int {
		if n < 2 {
			return n
		}
		return fibnocciClosure(n-1) + fibnocciClosure(n-2)
	}

	fmt.Println("Fibonacci Closure: n Fibonacci numbers: ", fibnocciClosure(6))

	// the shorthand declaration := cannot be used for recursively calling the function within itself because it attempts to reference the function before it's fully defined.
	var slice []int
	var addInts func(v int) int
	addInts = func(val int) int {
		if len(slice) > 5 {
			return len(slice)
		}
		slice = append(slice, val)
		return addInts(val + 1)
	}
	fmt.Println(slice)
	fmt.Println(addInts(3))
	fmt.Println(slice)

	return 1, 2, 3, 4
}
