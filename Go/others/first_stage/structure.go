package main

import "fmt"

// Structure is a collection of memebers of a different data types into a single variable
// Where as array stores multiple values of SAME data type into a single variable
// Struct is useful for grouping data together to create records
type Person struct {
	id   int
	name string
	dept string
}

type ExampleType struct {
	a int
	b int
}

// Accessing struct members
func accessMembers() {
	var pers1 Person // pers1 of type Person
	var pers2 Person

	pers1 = populatePerson(pers1)

	fmt.Printf("%v %T\n", pers1, pers2)

	/* Creating struct during declaration
	example := []struct {
		a int
		b bool
	}{
		{2, true},
		{3, false},
	}
	*/

	example := []ExampleType{
		{2, 20}, {3, 30},
	}

	fmt.Println(example)

}

func populatePerson(pers Person) Person {
	pers.id = 1
	pers.name = "Ramu"
	pers.dept = "CSE"
	return pers
}
