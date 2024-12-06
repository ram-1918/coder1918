package practice

import (
	"fmt"
	"math"
)

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

func Datatypes() {
	// 1. Variable declarations & data types
	fmt.Println("------------Datatypes-----------")

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
