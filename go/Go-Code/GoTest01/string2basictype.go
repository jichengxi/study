package main

import (
	"fmt"
	"strconv"
)

func main() {
	var str1 string = "true"
	var b bool
	b, _ = strconv.ParseBool(str1)
	fmt.Printf("b type %T b=%v \n", b, b)

	var str2 string = "123456789"
	var n1 int64
	n1, _ = strconv.ParseInt(str2, 10, 64)
	fmt.Printf("n1 type %T n1=%v \n", n1, n1)

	var str3 string = "123.456789"
	var n2 float64
	n2, _ = strconv.ParseFloat(str3, 64)
	fmt.Printf("n2 type %T n2=%v \n", n2, n2)
}
