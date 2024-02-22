package main

import (
	"fmt"
	"math"
)

/*
-- Compile time refers to translating code into an executable program
-- Concurrency is performing multiple things at the same time without effecting the final outcome

From Reddit: our microservice should reliable , support oauth2, logging, caching ,metrics, REST & gRPC , graceful shutdown

GO:
Features
1. Garbage collection
2. package system
3. first-class functions
4. lexical scope
5. a system call interface
6. immutable strings
7. It has no
	implicit numeric conversions, constructors/destructors,
	operator overloading, default parameter values,
	inheritance, generics, exceptions, annotations, thread-local storage
Go Syntax
---------
- Package Declaration
- import statements
- functions
- expressions and statements

Initialize: go mod init example.com/hello -> it creates a .mod file
Run a Go File: go run ./filename.go
Save program as an executable: go build ./filename.go

 1. Syntax is similar to c++. Compiled language. C is the direct influences of Go
 2. statically typed:
	1. Type Definition
	2. Type Checking: Compiler verifies type at compile time before the program runs, which means
		if helps to catch errors without any execution issues.
	3. Better tooling: Comde completion and refactoring works effectively with static types
3. Supports concurrency through Goroutines and channels.
4. Has Automatic garbage collection.
5. Go doesn't have classes and objects, though it has unique way of using OOPs.
7. Instead of classes, Go uses 'struct' to define data types and methods
attached to those struct to define behaviour
8. Go encourages 'composition' over 'inheritance', where you build complex objects by combining simpler ones.
9. It uses 'Interfaces' to define contracts for types, enabling abstraction and polymorphism.

Split the code base into multiple files but should be in the same package
(ex: package main, should be the first line for all files under one package)

To Run multiple files:
	1. go run *.go
	2. go run file1.go file2.go

// To get Strong in: Pointers, structs, garbage collection, Composition, Interfaces, Goroutines & channels



Benefits:
1. It excel in handling concurrent tasks, making it ideal for building responsive APIs.
2. Concept of channels eases the communication between goroutines, which helps in synchronization(all goroutines will be in sync)
*/

/*
1. variables are declared using var keyword or := sign
2. var variablename type = value => type is explicitly declared
3. var variablename = value or variablename := value => type is inferred
4. variable can be declared without initializing,
if this is the case,
then they will be initialized with the default value of its type(integer with 0, string with ” and ...)
5. Data types: int(8, 16, 32), uint(8, 16,32), float32, float64, bool, string
6. when a variable is declared, its value can be updated later in the code but with the same type value
7. We can declare many variables of one type in a single line.
*/

/**
1. Variable + constants declarations & data types
2. Functions
3. Data structures - Arrays, Slices, Maps, Structs
4. Type Systems - Pointers, Interfaces, type
5. Concurrency - Goroutines + Channels

others:
type conversions,

Integer type ranges:
int8   : -128 to 127 (2^7)
int16  : -32768 to 32767 (2^15)
int32  : -2147483648 to 2147483647 (2^31)
int64  : -9223372036854775808 to 9223372036854775807 (2^63)
uint8  : 0 to 255 (Pow(2, 8))
uint16 : 0 to 65535 (Pow(2, 16))
uint32 : 0 to 4294967295 (Pow(2, 32))
uint64 : 0 to 18446744073709551615 (Pow(2, 64))

value = 16 (2 ^ 4)
value >> 1 ~~ 2 ^ 3 => shifting bits right means reducing power of 2 by one
value << 1 ~~ vice-versa
*/

const MAXINT = ^uint8(0) // math.MinInt32 // or ^uint8(0)
const value = 16

func IntegersAndStrings() {
	// 1. Variable declarations & data types

	// Declaring Integers, floating-points, strings
	var intVariableName int8
	var floatVariablename float64 = 1.123 // declaration with initial values
	stringVariableName := "Some String"   // Variables declared using := operator, cannot be used outside the function

	fmt.Println("Level 1: ", MAXINT, value>>1, intVariableName, floatVariablename, stringVariableName, math.Pow(2, 15))

	// Important String methods
	// Strings are immutable: when an old list is assigned to a newone and any changes made to the new one doesnt reflect the previous one
	var str string = "test"
	str += " 1"

	var newstr string = str // Both doesnot refer to the same memory location
	newstr = "new str"

	fmt.Println("Level 2: ", str, &str, &newstr, newstr)

	// fmt.Println("Level 2: ", str, &str, newstr)

}

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
