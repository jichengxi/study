package main

import "fmt"

type Point struct {
	x int
	y int
}

func main() {
	var a interface{}
	var point Point = Point{1,2}
	a = point
	var b Point
	b = a.(Point)
	fmt.Println(b)

	var x interface{}
	var b2 float32 = 1.1
	x = b2
	y, ok := x.(float64)
	fmt.Println("ok=", ok)
	fmt.Println("y=", y)
}
