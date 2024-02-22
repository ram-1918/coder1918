package main

import (
	"fmt"
)

func main() {
	fmt.Println("main func() in others package")
	IntegersAndStrings()
	a, b, _, _ := Functions(10, 20)
	fmt.Println(a, b)
}
