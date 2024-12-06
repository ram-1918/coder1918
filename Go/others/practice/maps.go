package practice

import (
	"fmt"
)

func Maps() {
	fmt.Println("--------Maps---------")
	var map1 = make(map[int]int)
	map1[2] = 3
	var map2 = make(map[int][]int) // slice as value type, we can use an array instead as well
	res := []int{}
	res = append(res, 1, 3, 5)
	map2[2] = res
	// Array as Key Type, Cannot use slice as a Key type
	// Used for seen/visited nodes in Graph problems
	var map3 = make(map[[2]int]bool)
	resKey := [2]int{1, 2}
	map3[resKey] = true
	// Array as key: Created Key Type in advance
	type KeyType [2]int
	var map4 = make(map[KeyType]bool)
	map4[KeyType{1, 2}] = false
	// Implement Set using Maps => use map[type]struct{} instead of map[type]bool for saving bytes(space efficieny)
	map5 := map[int]bool{}
	map5[2] = true
	// to check if '2' exists
	if map5[2] {
		fmt.Println("Set using Boolean as value", map5)
	}
	// Using Structs
	map6 := make(map[int]struct{})
	map6[4] = struct{}{}
	if _, ok := map6[4]; ok {
		fmt.Println("Set with structs: ", map6)
	}

	fmt.Println(map1, map2, map3, map4)
}
