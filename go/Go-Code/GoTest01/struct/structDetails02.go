package main

import "fmt"

type Point struct {
	x int
	y int
}

type Rect struct {
	leftUp, rightDown Point
}

type Rect2 struct {
	leftUp, rightDown *Point
}

func main() {
	r1 := Rect{Point{1,2}, Point{3,4}}
	// r1有四个整数类型，在内存中是连续分布的
	fmt.Println("r1.leftUp.x的地址=", &r1.leftUp.x)
	fmt.Println("r1.leftUp.y的地址=", &r1.leftUp.y)
	fmt.Println("r1.rightDown.x的地址=", &r1.rightDown.x)
	fmt.Println("r1.rightDown.y的地址=", &r1.rightDown.y)

	r2 := Rect2{&Point{10,20}, &Point{30,40}}
	fmt.Println("r2.leftUp的地址=", &r2.leftUp)
	fmt.Println("r2.leftUp的地址=", &r2.rightDown)
}
