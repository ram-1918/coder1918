package main

import "fmt"

// Maps in Go are 'unordered' and 'changable' collection of elements that does not allow 'duplicates'
// multiple ways of creating maps
// Its default value is nil
// The output order is different because, The data is stored in way to have efficient retrieval from the map
// Allowed types
// Boolean, Int, float, string, struct, arrays, pointers, interfaces(as long as dynamic type supports equality)
// Not Allowed types
// functions, maps, slices; beacuse == operator is not defined for them

/*
Map
---
Create:
var map_name = map[keyType]valueType{k1: v1, k2: v2, k3: v3...}
map_name := map[keyType]valueType{k1:v1, k2:v2}

Create(Empty map):
var map_name = make(map[keyType]valueType)

Read:
value = map_name[key]

Update:
map_name[key] = new_value

Delete:
delete(map_name key)

If key exisits:
value_of_key, ifExisits := map_name[key]

Iterate over maps
for k, v := range map_name {
	fmt.Println(k, v)
}

Iterate over maps in specific order
var orderedKeys = [...]type{values} => array
				or
var orderedKeys = []string{} => slice
				or
var orderedKeys []string => slice different declaration

orderedKeys = append(orderedKeys, k1, k2, k3)

for _, key := range orderedKeys {
	fmt.Println(key, map_name[key])
}
*/

func hashmap() {
	// var hashmap = map[keyType]valueType{key1: value1,...}
	// hashmap := map[keyType]valueType{key1: value1, key2: value2...}
	map1 := map[string]int{"a": 1, "b": 2}
	// Create an empty map using make()
	// make() is the right way to create an empty map
	// var map2 map[int]int => also a way but not the right one
	map2 := make(map[int]int)
	fmt.Printf("%v, %T\n", map2, map2)
	map2[1] = 1
	map2[1] = 2     // update map value
	delete(map2, 1) // Delete map's key => delete(map_name, key)
	fmt.Printf("%v, %T\n", map2, map2)
	val_of_a, ifexisit := map1["a"]
	fmt.Printf("%v, %v\n", val_of_a, ifexisit)
	fmt.Printf("%v, %T\n", map1["a"], map1["a"])
}
