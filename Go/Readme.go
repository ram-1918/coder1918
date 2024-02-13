package main

/*
-- Compile time refers to translating code into an executable program
-- Concurrency is performing multiple things out-of-order, or at the same time without effecting the final outcome
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
5. Go doesn't have classes and objects, even though it has unique way of using OOPs.
7. Instead of classes, Go uses 'struct' to define data types and methods
attached to those struct to define behaviour
8. Go encourages 'composition' over 'inheritance', where you build complex objects by combining simpler ones.
9. It uses 'Interfaces' to define contracts for types, enabling abstraction and polymorphism.

Benefits:
1. It excel in handling concurrent tasks, making it ideal for building responsive APIs.
*/

/*
1. variables are declared using var keyword or := sign
2. var variablename type = value => type is explicitly declared
3. var variablename = value or variablename := value => type is inferred
4. variable can be declared without initializing,
if this is the case,
then they will be initialized with the default value of its type(integer with 0, string with ” and ...)
5. Data types: int, float32, bool, string
6. when a variable is declared, its value can be updated later in the code but with the same type value
7. We can declare many variables of one type in a single line.
*/
